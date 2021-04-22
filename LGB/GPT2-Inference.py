# !pip install transformers
import numpy as np
import torch
from transformers import (set_seed, TrainingArguments, Trainer, GPT2Config, GPT2Tokenizer, AdamW, get_linear_schedule_with_warmup, GPT2ForSequenceClassification)

class GPT2:

  def __init__:

    # Look for gpu to use. Will use `cpu` by default if no gpu found.
    self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # device = torch.device('cpu')
    print(device)
    model_path = "drive/MyDrive/Colab_datasets/LIAR-PLUS/GPT2-model"
    self.tokenizer = GPT2Tokenizer.from_pretrained(pretrained_model_name_or_path=model_path)
    self.gpt_model = GPT2ForSequenceClassification.from_pretrained(pretrained_model_name_or_path=model_path)
    self.gpt_model.eval()

  def predictGPT(text):

    self.gpt_model.to(device)
    inputs = self.tokenizer(sample_text, return_tensors="pt").to(self.device)
    outputs = gpt_model(**inputs)
    logits = outputs[0]
    predict_label = logits.argmax(axis=-1).flatten().tolist()
    return predict_label[0]