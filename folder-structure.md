```sh
│   .all-contributorsrc
│   .gitattributes
│   .gitignore
│   CODE_OF_CONDUCT.md
│   CONTRIBUTORS.md
│   fake_news_dataset.md
│   folder-structure.md
│   LICENSE
│   README.md
│   reference.md
│   requirements.txt
│   setup.sh
│   start-server.sh
│   stop-server.sh
│
├───.github
│       FUNDING.yml
│
├───Documentations
│   ├───Project Presentation II
│   │       Group 19 Final year project presentation.pptx
│   │
│   ├───Project-Presentation I
│   │       BE_Project_Presentation.pdf
│   │
│   ├───SDD
│   │       FYP_SDD.docx
│   │
│   ├───SPMP
│   │       FYP_SPMP.docx
│   │
│   ├───SRS
│   │       SRS.docx
│   │
│   ├───STD
│   │       FYP_STD.docx
│   │
│   └───Synopsis-report
│           Group19_BE_Project_Synopsis.docx
│
│
├───Models
│   ├───BERT_Fake_News_Classification
│   │   │   Bert_inference.py
│   │   │
│   │   ├───.model
│   │   │   └───uncased_L-12_H-768_A-12
│   │   │           bert_config.json
│   │   │           bert_model.ckpt.data-00000-of-00001
│   │   │           bert_model.ckpt.index
│   │   │           bert_model.ckpt.meta
│   │   │           vocab.txt
│   │   │
│   │   ├───notebook
│   │   │       Bert_model.ipynb
│   │   │
│   │   └───pretrained_weights
│   │           bert_news.h5
│   │
│   ├───Bidirectional_LSTM_Glove
│   │   │   inference.py
│   │   │   model_plot.png
│   │   │
│   │   ├───checkpoint
│   │   │       tokenizer.pickle
│   │   │
│   │   ├───model
│   │   │       Fake_News_Glove_Model.h5
│   │   │
│   │   └───notebook
│   │           Fake_News_Detection_GloVe.ipynb
│   │
│   ├───GPT2_Model
│   │   │   gpt2-inference-model.py
│   │   │
│   │   ├───model
│   │   │       config.json
│   │   │       merges.txt
│   │   │       pytorch_model.bin
│   │   │       special_tokens_map.json
│   │   │       tokenizer_config.json
│   │   │       vocab.json
│   │   │
│   │   └───notebook
│   │           GPT2_model.ipynb
│   │
│   └───Roberta_Model
│       ├───model
│       │   │   checkpoint-7500-epoch-5.zip
│       │   │
│       │   └───checkpoint-7500-epoch-5
│       │           config.json
│       │           merges.txt
│       │           model_args.json
│       │           optimizer.pt
│       │           pytorch_model.bin
│       │           scheduler.pt
│       │           special_tokens_map.json
│       │           tokenizer_config.json
│       │           training_args.bin
│       │           vocab.json
│       │
│       └───notebook
│               Roberta_model.ipynb
│
├───Server-BERT
│      bert-server.py
│      BertInference.py
│   
│
├───Server-GPT2
│      gpt-server.py
│      GPT2Inference.py
│
├───Server-LSTM
│      biLSTMInference.py
│      lstm-server.py
│
├───Server-ROBERT
│      robert-server.py
│      RobertInference.py
|
│
└───src
    │   app.py
    │   fake_news_list.csv
    │   Fake_news_site.csv
    │   media_fn_scraper.py
    │   model_service.py
    │   url_utils.py
    │
    ├───assets
    │   └───images
    │           fake-news.png
    │           guy_with_laptop.jpg
    │
    ├───json_local
        │   categories.json
        │   fake_news_sites.json
        │
        └───opensources
                sources.json
    

```
