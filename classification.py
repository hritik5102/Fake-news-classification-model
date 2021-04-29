from LGB.GPT2Inference import GPT2
from LGB.biLSTMInference import BiLSTM
from LGB.BertInference import Bert_Classifier


class LGB:

    def __init__(self):

        self.gpt = GPT2()
        self.bilstm = BiLSTM()
        self.bert = Bert_Classifier(max_seq_len=150, lr=1e-5)

    def predict(self, text):

        a = self.gpt.predict(text)
        b = self.bilstm.predict(text)
        c, loss = self.bert.predict(text)
        sum = int(a) + int(b) + int(c)
        return 1 if sum > 1 else 0


# The following code runs only while testing.
if __name__ == "__main__":

    print("runnning LGB model")
    sample = "Donald Trump was born in Pakistan as Dawood Ibrahim Khan New Delhi: A video has gone viral showing a Pakistani anchor claiming that US President-elect Donald Trump was born in Pakistan and not in the United States of America.  The report further alleged that Trump's original name is Dawood Ibrahim Khan. In the video, the Neo News anchor elaborated on Trump's journey from North Waziristan to England and then finally to Queens, New York.  Neo news had cited tweets and a picture on social media to back its claim. The video was broadcast last month but went viral after Trump’s election victory on November 8."
    lgb = LGB()
    if lgb.predict(sample):
        print("News article is REAL")
    else:
        print("News article is FAKE")
