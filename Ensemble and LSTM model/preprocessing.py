import numpy as np
import re
import string
import os
import pandas as pd
try:
    from gensim.models import Doc2Vec
    from gensim.models.doc2vec import LabeledSentence
    from gensim import utils
except ImportError:
    os.sys.exit(1)
from nltk.corpus import stopwords

path = None
if os.path.isdir('dataset'):
    path = os.path.join(os.getcwd(), 'dataset/train.csv')
else:
    os.sys.exit(1)


def cleaning(text):
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = text.lower().split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return (text)


def cleanup(text):
    text = cleaning(text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def constructLabeledSentences(data):
    sentences = []
    for index, row in data.iteritems():
        sentences.append(LabeledSentence(utils.to_unicode(
            row).split(), ['Text' + '_%s' % str(index)]))
    return sentences


def wordEmbeddings(vector_dimension=300):
    # os.remove('embedding_model')
    if not os.path.exists(os.path.join(os.getcwd(), 'embedding_model')):
        data = pd.read_csv(path)
        missing_rows = []
        for i in range(len(data)):
            if data.loc[i, 'text'] != data.loc[i, 'text']:
                missing_rows.append(i)
        data = data.drop(missing_rows).reset_index().drop(
            ['index', 'id'], axis=1)

        for i in range(len(data)):
            data.loc[i, 'text'] = cleanup(data.loc[i, 'text'])

        x = constructLabeledSentences(data['text'])
        y = data['label'].values

        # doc2vec transform
        text_model = Doc2Vec(min_count=1, window=5, vector_size=vector_dimension, sample=1e-4, negative=5, workers=7, epochs=10,
                             seed=1)
        text_model.build_vocab(x)
        text_model.train(x, total_examples=text_model.corpus_count,
                         epochs=text_model.iter)
        # data set split for samples
        train_size = int(0.8 * len(x))
        test_size = len(x) - train_size

        text_train_arrays = np.zeros((train_size, vector_dimension))
        text_test_arrays = np.zeros((test_size, vector_dimension))
        train_labels = np.zeros(train_size)
        test_labels = np.zeros(test_size)

        for i in range(train_size):
            text_train_arrays[i] = text_model.docvecs['Text_' + str(i)]
            train_labels[i] = y[i]

        j = 0
        for i in range(train_size, train_size + test_size):
            text_test_arrays[j] = text_model.docvecs['Text_' + str(i)]
            test_labels[j] = y[i]
            j = j + 1
        text_model.save('embedding_model')
        return text_train_arrays, text_test_arrays, train_labels, test_labels
    else:
        test_model = Doc2Vec.load(os.path.join(
            os.getcwd(), 'embedding_model.wv.vectors.npy'))
        print(test_model)

# for DL


def clean_data():
    path = os.path.join(os.getcwd(), 'train.csv')
    vector_dimension = 300

    data = pd.read_csv(path)

    missing_rows = []  # remove missing values / tuples
    for i in range(len(data)):
        if data.loc[i, 'text'] != data.loc[i, 'text']:
            missing_rows.append(i)
    data = data.drop(missing_rows).reset_index().drop(['index', 'id'], axis=1)

    for i in range(len(data)):
        data.loc[i, 'text'] = cleanup(data.loc[i, 'text'])

    data = data.sample(frac=1).reset_index(drop=True)

    x = data.loc[:, 'text'].values
    y = data.loc[:, 'label'].values

    train_size = int(0.8 * len(y))
    test_size = len(x) - train_size

    xtr = x[:train_size]
    xte = x[train_size:]
    ytr = y[:train_size]
    yte = y[train_size:]

    np.save('xtr_shuffled.npy', xtr)
    np.save('xte_shuffled.npy', xte)
    np.save('ytr_shuffled.npy', ytr)
    np.save('yte_shuffled.npy', yte)


wordEmbeddings()
