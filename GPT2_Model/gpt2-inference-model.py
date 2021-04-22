import os
import numpy as np
import torch
from transformers import (GPT2Tokenizer, GPT2ForSequenceClassification)

# Look for gpu to use. Will use `cpu` by default if no gpu found.
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

_ROOT = os.path.abspath(os.path.dirname(__file__))

model_path = os.path.join(_ROOT, 'model')

# Creating a tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(
    pretrained_model_name_or_path=model_path)

# Model
gpt_model = GPT2ForSequenceClassification.from_pretrained(
    pretrained_model_name_or_path=model_path)

# Evaluation
gpt_model.eval()


def predictGPT(text):
    gpt_model.to(device)
    inputs = tokenizer(text, return_tensors="pt").to(device)
    outputs = gpt_model(**inputs)
    logits = outputs[0]
    predict_label = logits.argmax(axis=-1).flatten().tolist()
    return predict_label[0]


# sample_text = 'When asked by a reporter whether hes at the center of a criminal scheme to violate campaign laws, Gov. Scott Walker nodded yes.'
# print(predictGPT(sample_text))
