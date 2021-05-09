import os

# For Removing this warning : "Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found" 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import logging
logging.getLogger('tensorflow').disabled = True

# "0" means no logging. # For Removing XLA warnings
import tensorflow as tf
tf.autograph.set_verbosity(0)

import re
import bert
import numpy as np
from tensorflow import keras
from bert.loader import StockBertConfig, map_stock_config_to_params, load_stock_weights
from bert.tokenization.bert_tokenization import FullTokenizer
from bert.model import BertModelLayer


class Bert_Classifier:

    def __init__(self, max_seq_len, lr):
        
        _ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.bert_ckpt_dir = os.path.join(_ROOT, "Models","BERT_Fake_News_Classification",".model","uncased_L-12_H-768_A-12")
        self.bert_ckpt_file = os.path.join(
            self.bert_ckpt_dir, "bert_model.ckpt")
        self.bert_config_file = os.path.join(
            self.bert_ckpt_dir, "bert_config.json")
        self.max_seq_len = max_seq_len
        self.lr = lr
        self.bert_weight = os.path.join(_ROOT,"Models","BERT_Fake_News_Classification","pretrained_weights","bert_news.h5")

    def clean_txt(self, text):
        text = re.sub("'", "", text)
        text = re.sub("(\\W)+", " ", text)
        text = text.lower()
        return text

    def get_split(self, text):
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

    def create_model(self):
        """
        Creates a BERT classification model.
        The model architecutre is raw input -> BERT input -> drop out layer to prevent overfitting -> dense layer that outputs predicted probability.
        max_seq_len: the maximum sequence length
        lr: learning rate of optimizer
        """

        # create the bert layer
        with tf.io.gfile.GFile(self.bert_config_file, "r") as reader:
            bc = StockBertConfig.from_json_string(reader.read())
            bert_params = map_stock_config_to_params(bc)
            bert = BertModelLayer.from_params(bert_params, name="bert")

        input_ids = keras.layers.Input(
            shape=(self.max_seq_len,), dtype='int32', name="input_ids")
        output = bert(input_ids)

        # print("bert shape", output.shape)
        cls_out = keras.layers.Lambda(lambda seq: seq[:, 0, :])(output)
        # Dropout layer
        cls_out = keras.layers.Dropout(0.8)(cls_out)
        # Dense layer with probibility output
        logits = keras.layers.Dense(units=2, activation="softmax")(cls_out)

        model = keras.Model(inputs=input_ids, outputs=logits)
        model.build(input_shape=(None, self.max_seq_len))

        # load the pre-trained model weights
        load_stock_weights(bert, self.bert_ckpt_file)

        model.compile(optimizer=keras.optimizers.Adam(learning_rate=self.lr),
                      loss=keras.losses.SparseCategoricalCrossentropy(
                          from_logits=True),
                      metrics=[keras.metrics.SparseCategoricalAccuracy(name="acc")])

        model.summary()

        return model

    def predict(self, text):
        """
        Predict new document using the trained model. 
        doc: input document in format of a string
        """

        # clean the text
        doc = self.clean_txt(text)

        # split the string text into list of subtexts
        doc = self.get_split(doc)

        # tokenize the subtexts as well as padding
        tokenizer = FullTokenizer(
            vocab_file=os.path.join(self.bert_ckpt_dir, "vocab.txt"))
        pred_tokens = map(tokenizer.tokenize, doc)
        pred_tokens = map(lambda tok: ["[CLS]"] + tok + ["[SEP]"], pred_tokens)
        pred_token_ids = list(
            map(tokenizer.convert_tokens_to_ids, pred_tokens))
        pred_token_ids = map(lambda tids: tids +
                             [0]*(self.max_seq_len-len(tids)), pred_token_ids)
        pred_token_ids = np.array(list(pred_token_ids))

        # create model and load previous weights
        model = self.create_model()
        model.load_weights(self.bert_weight)

        # predict the subtexts and average the prediction
        predictions = model.predict(pred_token_ids)
        predictions = predictions[:, 1]
        avg_pred = predictions.mean()
        if avg_pred > 0.5:
            doc_label = 0
        else:
            doc_label = 1

        return doc_label, avg_pred


# The following code runs only while testing.
if __name__ == "__main__":

    input_text = "Donald Trump was born in Pakistan as Dawood Ibrahim Khan New Delhi: A video has gone viral showing a Pakistani anchor claiming that US President-elect Donald Trump was born in Pakistan and not in the United States of America.  The report further alleged that Trump's original name is Dawood Ibrahim Khan. In the video, the Neo News anchor elaborated on Trump's journey from North Waziristan to England and then finally to Queens, New York.  Neo news had cited tweets and a picture on social media to back its claim. The video was broadcast last month but went viral after Trump’s election victory on November 8."
    obj = Bert_Classifier(max_seq_len=150, lr=1e-5)
    print(obj.predict(input_text))
