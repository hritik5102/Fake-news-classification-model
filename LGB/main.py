from GPT2Inference import GPT2 
from biLSTMInference import BiLSTM
from BertInference import Bert_Classifier

print("runnning script")

sample = "Donald Trump was born in Pakistan as Dawood Ibrahim Khan New Delhi: A video has gone viral showing a Pakistani anchor claiming that US President-elect Donald Trump was born in Pakistan and not in the United States of America.  The report further alleged that Trump's original name is Dawood Ibrahim Khan. In the video, the Neo News anchor elaborated on Trump's journey from North Waziristan to England and then finally to Queens, New York.  Neo news had cited tweets and a picture on social media to back its claim. The video was broadcast last month but went viral after Trump’s election victory on November 8."

gpt = GPT2()
label = gpt.predict(sample)
print("GPT2: ", label)

bilstm = BiLSTM()
label = bilstm.predict(sample)
print("BiLSTM: ", label)

bert = Bert_Classifier(max_seq_len=150, lr=1e-5)
label, loss = bert.predict(sample)
print("BERT: ", label)