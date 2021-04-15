# library for regular expression operations
from sklearn.metrics import (classification_report,                  # Metrics for calculation
                             confusion_matrix,
                             accuracy_score)
from tensorflow.keras.callbacks import (EarlyStopping,                # Checkpoints
                                        ReduceLROnPlateau,
                                        ModelCheckpoint,
                                        TensorBoard)
from sklearn.model_selection import train_test_split                  # Train
from sklearn.feature_extraction.text import CountVectorizer           # Bag of words
from tensorflow.keras.layers import Bidirectional                     # BiDirectional
from tensorflow.keras.layers import Dense                             # Dense layer
from tensorflow.keras.layers import Dropout                           # Dropout
from tensorflow.keras.layers import LSTM                              # LSTM
from tensorflow.keras.layers import Embedding                         # Embeddings
from tensorflow.keras.preprocessing.sequence import pad_sequences     # Pad Sequence
from tensorflow.keras.preprocessing.text import Tokenizer             # Tokenizer keras
from tensorflow.keras.preprocessing.text import one_hot               # One hot vector
from tensorflow.keras.models import Sequential
import re

# NLP library for features NER, POS tagging, dependency parsing
import warnings                             # For removing "Warnings"
import gc
import nltk                                         # Python library for NLP
import contractions                                 # contraction libary
import unicodedata                                  # charachter encoding library
from nltk.stem import WordNetLemmatizer             # module for Lemmatizer
from nltk.corpus import stopwords                   # stopwords
from nltk.tokenize import TweetTokenizer
from textblob import TextBlob, Word                 # textBlob library
# module for tokenizing strings

# module for stop words that come with NLTK
from nltk.corpus import stopwords
import string                                       # for string operations

# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd
import numpy as np                                  # linear algebra
import matplotlib.pyplot as plt                     # library for visualization
warnings.filterwarnings("ignore")

# Sequential model

# Render a dependency parse tree or named entity visualization


# download the stopwords from NLTK
nltk.download('stopwords')
nltk.download('wordnet')                            # Wordnet
nltk.download('averaged_perceptron_tagger')         # POS Tagger
nltk.download('punkt')


try:
    with open('./checkpoint/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
        print("Hello")
except Exception:
    print("Error in loading file")
