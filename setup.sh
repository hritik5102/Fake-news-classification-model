#!/bin/bash

echo -e "[INFO] Installing Requirements ...\n"
pip3 install -r requirements.txt

# echo -e "[INFO] BERT model setup  ...\n"

# echo -e "[INFO] Creating a model folder ...\n"
# mkdir -p Models/BERT_Fake_News_Classification/.model/uncased_L-12_H-768_A-12

# echo -e "[INFO] Downloading BERT Model ...\n"
# gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_config.json Models/BERT_Fake_News_Classification/.model/uncased_L-12_H-768_A-12
# gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/vocab.txt Models/BERT_Fake_News_Classification/.model/uncased_L-12_H-768_A-12
# gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.meta Models/BERT_Fake_News_Classification/.model/uncased_L-12_H-768_A-12
# gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.index Models/BERT_Fake_News_Classification/.model/uncased_L-12_H-768_A-12
# gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.data-00000-of-00001 Models/BERT_Fake_News_Classification/.model/uncased_L-12_H-768_A-12

# echo -e "[INFO] Downloading Pretrained weights ...\n"
# mkdir -p Models/BERT_Fake_News_Classification/pretrained_weights
# gdown --id 1pI12nFTsNdcoAY-tEyuybuYgP8kKOILA
# mv bert_news.h5 Models/BERT_Fake_News_Classification/pretrained_weights

echo -e "[INFO] Installing pytorch dependency ...\n"
pip3 install torch==1.8.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

echo -e "[INFO] GPT2 model setup  ...\n"

echo -e "[INFO] Installing GPT Model dependency ...\n"
gdown --id 11XNr5K9IFmWSQdmidC6rIBKTlP361VNT
mkdir -p Models/GPT2_Model/model
unzip -o model.zip -d Models/GPT2_Model/model
rm model.zip

echo -e "[INFO] Installing Roberta Model dependency ...\n"
gdown --id 1iKuZFlfKQmPV917CNrAVHZOxZjYA5Ck_
mkdir -p Models/Roberta_Model/model
unzip -o model.zip -d Models/Roberta_Model/model
rm model.zip
