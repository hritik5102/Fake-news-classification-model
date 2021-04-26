# !pip install transformers
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
        model_path = "GPT2_Model\model"
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
