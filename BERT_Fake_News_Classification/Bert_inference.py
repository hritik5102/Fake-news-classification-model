import numpy as np
import urllib
import json
import pandas as pd
import os
from tqdm import tqdm
import tensorflow as tf
from tensorflow import keras
import bert
from bert.model import BertModelLayer
from bert.loader import StockBertConfig, map_stock_config_to_params, load_stock_weights
from bert.tokenization.bert_tokenization import FullTokenizer
import re

# tf.keras.models.load_model(path, custom_objects={"BertModelLayer": bert.BertModelLayer})


def clean_txt(text):
    text = re.sub("'", "", text)
    text = re.sub("(\\W)+", " ", text)
    text = text.lower()
    return text


def get_split(text):
    """
    Split each news text to subtexts no longer than 150 words.
    """
    l_total = []
    l_parcial = []
    if len(text.split())//120 > 0:
        n = len(text.split())//120
    else:
        n = 1
    for w in range(n):
        if w == 0:
            l_parcial = text.split()[:150]
            l_total.append(" ".join(l_parcial))
        else:
            l_parcial = text.split()[w*120:w*120 + 150]
            l_total.append(" ".join(l_parcial))
    return l_total


'''
# gsutil is a part of google SDK and python application used to access and manage cloud storage
# form the command line. some of the major operation performed using gsutil are 

    - Listing bucket and object
    - Creating a bucket 
    - Uploading and downloading and deleting objects
    - Manage labels
    - Rename & Delete Bucket
'''

# Reference : https://cloud.google.com/sdk/docs/downloads-interactive
bert_model_name = "uncased_L-12_H-768_A-12"
bert_ckpt_dir = os.path.join(".model/", bert_model_name)
bert_ckpt_file = os.path.join(bert_ckpt_dir, "bert_model.ckpt")
bert_config_file = os.path.join(bert_ckpt_dir, "bert_config.json")


def create_model(max_seq_len, lr=1e-5):
    """
    Creates a BERT classification model. 
    The model architecutre is raw input -> BERT input -> drop out layer to prevent overfitting -> dense layer that outputs predicted probability.

    max_seq_len: the maximum sequence length
    lr: learning rate of optimizer
    """

    # create the bert layer
    with tf.io.gfile.GFile(bert_config_file, "r") as reader:
        bc = StockBertConfig.from_json_string(reader.read())
        bert_params = map_stock_config_to_params(bc)
        bert = BertModelLayer.from_params(bert_params, name="bert")

    input_ids = keras.layers.Input(
        shape=(max_seq_len,), dtype='int32', name="input_ids")
    output = bert(input_ids)

    print("bert shape", output.shape)
    cls_out = keras.layers.Lambda(lambda seq: seq[:, 0, :])(output)
    # Dropout layer
    cls_out = keras.layers.Dropout(0.8)(cls_out)
    # Dense layer with probibility output
    logits = keras.layers.Dense(units=2, activation="softmax")(cls_out)

    model = keras.Model(inputs=input_ids, outputs=logits)
    model.build(input_shape=(None, max_seq_len))

    # load the pre-trained model weights
    load_stock_weights(bert, bert_ckpt_file)

    model.compile(optimizer=keras.optimizers.Adam(learning_rate=lr),
                  loss=keras.losses.SparseCategoricalCrossentropy(
                      from_logits=True),
                  metrics=[keras.metrics.SparseCategoricalAccuracy(name="acc")])

    model.summary()

    return model


model = create_model(max_seq_len=150, lr=1e-5)

model.load_weights("pretrained_model/bert_news.h5")


def predict_new(doc, model, max_seq_len=150):
    """
    Predict new document using the trained model. 

    doc: input document in format of a string
    """

    # clean the text
    doc = clean_txt(doc)
    # split the string text into list of subtexts
    doc = get_split(doc)
    # tokenize the subtexts as well as padding
    tokenizer = FullTokenizer(
        vocab_file=os.path.join(bert_ckpt_dir, "vocab.txt"))
    pred_tokens = map(tokenizer.tokenize, doc)
    pred_tokens = map(lambda tok: ["[CLS]"] + tok + ["[SEP]"], pred_tokens)
    pred_token_ids = list(map(tokenizer.convert_tokens_to_ids, pred_tokens))
    pred_token_ids = map(lambda tids: tids +
                         [0]*(max_seq_len-len(tids)), pred_token_ids)
    pred_token_ids = np.array(list(pred_token_ids))

    # create model and load previous weights
    # model = create_model(max_seq_len = data.max_seq_len)
    # model.load_weights()

    # predict the subtexts and average the prediction
    predictions = model.predict(pred_token_ids)
    predictions = predictions[:, 1]
    avg_pred = predictions.mean()
    if avg_pred > 0.5:
        doc_label = 'fake'
    else:
        doc_label = 'Real'

    return doc_label, avg_pred


def load_convert_data(url):
    """
    Downloads the json file from net and convert into pandas dataframe format.
    """
    with urllib.request.urlopen(url) as url:
        df = json.loads(url.read().decode())
        df = pd.DataFrame.from_dict(df)

    return df


# Run an example text from original test set
fake_test = load_convert_data(
    "https://storage.googleapis.com/public-resources/dataset/fake_test.json")
doc = fake_test['text'][7]
print('----------------------NEWS -----------------------')
print(doc)
doc_label, avg_pred = predict_new(doc, model, 150)
print()
print('---------------- PREDICTION RESULTS --------------')
print('The predicted probability of news being FAKE is ', avg_pred)
print('CLASSIFICATION : The predicted label of news is ', doc_label.upper())
