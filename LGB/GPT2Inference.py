# !pip install transformers
import os
# For Removing this warning : "Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found" 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import logging
logging.getLogger('tensorflow').disabled = True

import numpy as np
import torch
from transformers import (set_seed, TrainingArguments, Trainer, GPT2Config, GPT2Tokenizer,
                          AdamW, get_linear_schedule_with_warmup, GPT2ForSequenceClassification)


class GPT2:

    def __init__(self):

        # Look for gpu to use. Will use `cpu` by default if no gpu found.
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # device = torch.device('cpu')
        print("Device: ", self.device)
        _ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(_ROOT, "Models","GPT2_Model","model")
        self.tokenizer = GPT2Tokenizer.from_pretrained(
            pretrained_model_name_or_path=model_path)
        self.gpt_model = GPT2ForSequenceClassification.from_pretrained(
            pretrained_model_name_or_path=model_path)
        self.gpt_model.eval()

    def predict(self, text):

        self.gpt_model.to(self.device)
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        outputs = self.gpt_model(**inputs)
        logits = outputs[0]
        predict_label = logits.argmax(axis=-1).flatten().tolist()
        return predict_label[0]

if __name__ == '__main__':
    obj = GPT2()
    sample = "Donald Trump was born in Pakistan as Dawood Ibrahim Khan New Delhi: A video has gone viral showing a Pakistani anchor claiming that US President-elect Donald Trump was born in Pakistan and not in the United States of America.  The report further alleged that Trump's original name is Dawood Ibrahim Khan. In the video, the Neo News anchor elaborated on Trump's journey from North Waziristan to England and then finally to Queens, New York.  Neo news had cited tweets and a picture on social media to back its claim. The video was broadcast last month but went viral after Trump’s election victory on November 8."
    print(obj.predict(sample))
