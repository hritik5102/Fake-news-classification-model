echo -e "Creating a model folder ...\n"
mkdir -p .model .model/uncased_L-12_H-768_A-12

echo -e "Downloading BERT Model ...\n"
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_config.json .model/uncased_L-12_H-768_A-12
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/vocab.txt .model/uncased_L-12_H-768_A-12
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.meta .model/uncased_L-12_H-768_A-12
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.index .model/uncased_L-12_H-768_A-12
gsutil cp gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12/bert_model.ckpt.data-00000-of-00001 .model/uncased_L-12_H-768_A-12

ls -la .model .model/uncased_L-12_H-768_A-12

echo -e "Downloading Pretrained weights ...\n"

mkdir pretrained_model 

wget https://www.dropbox.com/s/7vf4oqti3abvbz4/bert_news.h5 -P /pretrained_model


# mkdir pretrained_model 

# sudo wget https://www.dropbox.com/s/7vf4oqti3abvbz4/bert_news.h5 -P /pretrained_model

mkdir pretrained_model 
sudo wget https://www.dropbox.com/s/7vf4oqti3abvbz4/bert_news.h5  --directory-prefix  ~/pretrained_model


# mkdir pretrained_model 

# gdown --id 1pI12nFTsNdcoAY-tEyuybuYgP8kKOILA

# mv bert_news.h5 ~/pretrained_model