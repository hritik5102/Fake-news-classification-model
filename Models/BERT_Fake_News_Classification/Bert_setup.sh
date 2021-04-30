#!/bin/bash

echo -e "[INFO] Creating a model folder ...\n"
mkdir -p .model .model/uncased_L-12_H-768_A-12

echo -e "[INFO] Downloading BERT Model ...\n"
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_config.json .model/uncased_L-12_H-768_A-12
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/vocab.txt .model/uncased_L-12_H-768_A-12
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.meta .model/uncased_L-12_H-768_A-12
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.index .model/uncased_L-12_H-768_A-12
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.data-00000-of-00001 .model/uncased_L-12_H-768_A-12

ls -la .model .model/uncased_L-12_H-768_A-12

echo -e "[INFO] Downloading Pretrained weights ...\n"

mkdir pretrained_weights

gdown --id 1pI12nFTsNdcoAY-tEyuybuYgP8kKOILA

mv bert_news.h5 pretrained_weights

echo -e "[INFO] Installing pytorch dependency ...\n"
pip3 install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html