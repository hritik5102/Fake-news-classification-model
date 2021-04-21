# library for regular expression operations
from textblob import TextBlob, Word                 # textBlob library
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer             # module for Lemmatizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup                       # Scrapping article
import contractions                                 # contraction libary
import unicodedata                                  # charachter encoding library
import nltk                                         # Python library for NLP
from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer             # Tokenizer keras
from tensorflow.keras.preprocessing.sequence import pad_sequences     # Pad Sequence
import re
import os
import string                                       # for string operations
import pickle
import warnings
warnings.filterwarnings("ignore")

# download the stopwords from NLTK
nltk.download('stopwords')
nltk.download('wordnet')                            # Wordnet
nltk.download('averaged_perceptron_tagger')         # POS Tagger
nltk.download('punkt')


def process_text(content, stopwords_english):
    """Process tweet function.
        Input:
            content: a string containing a text
        Output:
            content_clean: a list of words containing the processed text
        """
    # Removing Accented Characters (Words such as résumé, café, prótest, divorcé, coördinate, exposé, latté etc.)
    content = unicodedata.normalize('NFKD', content).encode(
        'ascii', 'ignore').decode('utf-8', 'ignore')

    # Decontraction : aren't -> are not
    content = contractions.fix(content)

    # Remove HTML Element : <br/>, <hr/>, <p/>
    content = BeautifulSoup(content, 'lxml').get_text()

    # remove stock market tickers like $GE
    content = re.sub(r'\$\w*', '', content)

    # remove old style retweet text "RT"
    content = re.sub(r'^RT[\s]+', '', content)

    # remove hyperlinks
    content = re.sub(r'https?:\S+', '', content)

    # to remove other url links (like tim@gmail.com, abcnews.com etc)
    content = re.sub(
        r'[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', content, flags=re.MULTILINE)

    # Replaces #hashtag with hashtag
    # content = re.sub(r'#(\S+)', r'\1', content)

    # Replace @user with @user, or @@user with @user
    content = re.sub(r'[@]*(\S+)', r'\1', content)

    # Replace digit or digit before string (like 6pm) or string before digit ( like Hello123) with empty string
    content = re.sub('\w*\d\w*', '', content)

    # Multiline comment
    content = re.sub(r'/\*[^*]*(?:\*(?!/)[^*]*)*\*/',
                     '', content, flags=re.S)

    # funnnnny --> funny
    content = re.sub(r'(.)\1+', r'\1\1', content)

    # Replace multiple spaces with a single space or Removing extra whitespaces and tabs
    # content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'^\s*|\s\s*', ' ', content).strip()

    # remove line break '\n'
    content = re.sub(r"(?<=[a-z])\r?\n", " ", content)

    # tokenize content
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)

    content_tokens = tokenizer.tokenize(content)

    content_clean = []
    for word in content_tokens:
        # remove stopwords and punctuation
        if (word not in stopwords_english and word not in string.punctuation):
            content_clean.append(word)

        # Lammetizer
    sent = TextBlob(" ".join(content_clean))
    tag_dict = {"J": 'a',
                "N": 'n',
                "V": 'v',
                "R": 'r'}

    words_and_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]
    lemmatized_list = [wd.lemmatize(tag) for wd, tag in words_and_tags]
    return " ".join(lemmatized_list)


def bidirectional_glove_test(input_text):
    '''
    Input : Combination of article title and text
    Output : Binary Classification (Fake : 0 and Real : 1)
    '''

    stopwords_english = stopwords.words('english')

    # The word which we don't want to remove
    operators = set(('not', 'against', 'because',
                    'until', 'against', 'between', 'during', 'into', 'before', 'after', 'no', 'nor', 'won'))

    # Remove this word from stopwords
    stopwords_english = set(stopwords_english) - operators

    _ROOT = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(_ROOT, 'checkpoint', 'tokenizer.pickle'), 'rb') as handle:
        tokenizer = pickle.load(handle, encoding="latin1")

    process_fact_check = process_text(input_text, stopwords_english)

    # Tokenizer (text to sequences)
    fact_check_sequence = tokenizer.texts_to_sequences(
        texts=[process_fact_check])

    # Dataloader
    max_len = 500

    # now applying padding to make them even shaped.
    fact_check_padding = pad_sequences(
        sequences=fact_check_sequence, maxlen=max_len, padding='pre')

    # Load model
    model = load_model(os.path.join(
        _ROOT, 'model', 'Fake_News_Glove_Model.h5'))

    # Prediction
    result = model.predict_classes(fact_check_padding)

    return result[0][0]


# fact_check = "Donald Trump was born in Pakistan as Dawood Ibrahim Khan New Delhi: A video has gone viral showing a Pakistani anchor claiming that US President-elect Donald Trump was born in Pakistan and not in the United States of America.  The report further alleged that Trump's original name is Dawood Ibrahim Khan. In the video, the Neo News anchor elaborated on Trump's journey from North Waziristan to England and then finally to Queens, New York.  Neo news had cited tweets and a picture on social media to back its claim. The video was broadcast last month but went viral after Trump’s election victory on November 8."
# print(bidirectional_glove_test(fact_check))
