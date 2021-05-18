import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import logging
logging.getLogger('tensorflow').disabled = True
import tensorflow as tf
tf.autograph.set_verbosity(0)
import re

from simpletransformers.classification import ClassificationModel, ClassificationArgs

class Robert:

    def __init__(self):

        _ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(_ROOT, "Models","Roberta_Model","model","checkpoint-7500-epoch-5")
        # model_path = "Models/Roberta_Model/model/checkpoint-7500-epoch-5"
        self.model = ClassificationModel("roberta", model_path, use_cuda = False)

    def clean_txt(self, text):
        text = re.sub("'", "", text)
        text = re.sub("(\\W)+", " ", text)
        text = text.lower()
        return text

    def predict(self, text):

        sample = self.clean_txt(text)
        label, raw_outputs = self.model.predict([sample])

        return label[0]

if __name__ == '__main__':

    sample = """ Chinese President Xi Jinping on Friday offered help to India in the fight against the coronavirus pandemic, Chinese state media reported.According to China's state media agency Xinhua, President Xi Jinping also "extended condolences" to Prime Minister Narendra Modi over the Covid-19 pandemic in India. President Xi Jinping sent a message of condolences to Indian Prime Minister Narendra Modi over the Covid-19 pandemic in the country, Xinhua reported. In his message, President Xi Jinping said China is "willing to strengthen" anti-pandemic cooperation with India, and provide support and help. This development comes amid strained relations between India and China for nearly a year over the standoff in Eastern Ladakh and violent clashes between the two sides. India is currently reeling under the second wave of coronavirus infections and has been consistently recording over 3,00,000 new cases every day. The death too has mounted as hospitals are facing an acute shortage of oxygen-supported beds, ICU beds, ventilators and medical oxygen. Chinese Ambassador to India, Sun Weidong in a series of tweets said the Chinese President has sent a message of sympathy to Prime Minister Narendra Modi. Chinese President Xi Jinping sends a message of sympathy to Indian Prime Minister Narendra Modi today. President Xi says, 'I am very concerned about the recent situation of Covid-19 pandemic in India. On behalf of the Chinese Government and people, as well as in my own name, I would like to express sincere sympathies to the Indian Government and people."""

    robert = Robert()
    result = robert.predict(sample)

    print(result)