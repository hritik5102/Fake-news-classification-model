## **Fake news dataset**

- [LIAR Dataset](#LIAR-Dataset)
- [Buzzfeed](#Buzzfeed)
- [PHEME and CREDBANK](#PHEME-and-CREDBANK)
- [BS Detector](#BS-Detector)
- [Politifact](#Politifact)
- [Fake News Challenge dataset](#Fake-News-Challenge-dataset)
- [Fact Extraction and verification (FEVER) dataset](<#Fact-Extraction-and-verification-(FEVER)-dataset>)
- [Fake news dataset](#Fake-news-dataset)
- [FakeNewsNet dataset](#FakeNewsNet-dataset)
- [ClaimBuster dataset](#ClaimBuster-dataset)
- [SOME-LIKE-IT-HOAX](#SOME-LIKE-IT-HOAX)
- [MultiFC Dataset](#MultiFC-Dataset)
- [ISOT-Fake-News-Dataset](#ISOT-Fake-News-Dataset)

## **LIAR Dataset**

LIAR : contains short political statements, obtained through the website PolitiFact.com.
Each statement is annotated with the author, the context, a veracity label and a justification for such label.
LIAR Dataset [11]: The dataset includes 12,836 short statements labelled for truthfulness, subject, context/venue, speaker, state, party, and prior history. Table 1 provides the details of LIAR dataset

LIAR is one of the largest publicly available fake news datasets. It has been constructed from a collection of statements investigated by experts in politifact.com, which is a well-known fact-checking service. The author did split the dataset into three sets: train, test, and development. His sample selection for sets is random where the train, test, and development sets contain, respectively, 80%, 10%, and 10% of the entire dataset.

He statements are short sentence(s), mostly from American politicians covering different topics. The statements have been manually classified into six classes including

**a. True**
**b. Mostly True**
**c. Half-True**
**d. Barely-True**
**e. False**
**f. Pants-on-Fire**

**Reference**:

- [Github - Tariq60/LIAR-PLUS](https://github.com/Tariq60/LIAR-PLUS/tree/master/dataset)

- [Github - thiagorainmaker77/liar](https://github.com/thiagorainmaker77/liar)

- [LIAR Dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip)

## Buzzfeed

Buzzfeed : BUZZFEEDNEWS5 collects 2,282 posts from 9 news agencies on Facebook. Each post is factchecked by 5 BuzzFeed journalists.

The advantages of this dataset are that the articles are collected from both sides of left-leaning and right-leaning organizations. There are two enriched versions of BUZZFEEDNEWS: Potthast et al. (2017) enriched them by adding data such as the linked articles, and BUZZFACE (Santia and Williams, 2018) extends the BuzzFeed dataset with the 1.6 million comments related to news articles on Facebook.

The authors in [73] have focused on Facebook publishers. starting from BuzzFeed, the collected data contain URLs from posts produced by nine verified Facebook publishers (3 mainstream publishers, and 6 hyperpartisan publishers). Each post is manually fact checked and annotated for correctness by BuzzFeed journalists.

This dataset comprises a complete sample of news published in Facebook from 9 news agencies over a week close to the 2016 U.S. election from September 19 to 23 and September 26 and 27. Every post and the linked article were fact-checked claim-by-claim by 5 BuzzFeed journalists. It contains 1,627 articles 826 mainstream, 356 left-wing, and 545 right-wing articles.

Dataset includes : Images (url of the post , no. of likes

**Reference** :

- [Github - BuzzFeedNews/2016-10-facebook-fact-check](https://github.com/BuzzFeedNews/2016-10-facebook-fact-check)

## PHEME and CREDBANK

**PHEME and CREDBANK are two Twitter datasets.**

**PHEME**: PHEME contains 330 twitter threads (a series of connected Tweets from one person) of nine newsworthy events, labeled as true or false.
It is a repository of rumors and non-rumors generated on Twitter during breaking news.

**CREDBANK**: is a large scale dataset, containing 60 million tweets. Tweets are grouped into events by means of topic modelling techniques. Each event is annotated for credibility via Mechanical Turk. Although a credibility judgment cannot be directly associated with a veracity score, it may be used as a good approximation for veracity classification.

CREDBANK contains 60 million tweets covering 96 days, grouped into 1,049 events with a 30-dimensional vector of truthfulness labels. Each event was rated on a
5-point Likert scale of truthfulness by 30 human annotators. They concatenate 30 ratings as a vector because they find it difficult to reduce it to a one-dimensional score.

As mentioned above, these datasets were created for verifying the truthfulness of tweets. Thus they are limited to a few topics and can include tweets with no relationship to news. Hence both datasets are not ideal for fake news detection, and they are more frequently used for rumor detection

**Reference :**

- [PHEME Dataset](https://figshare.com/articles/PHEME_dataset_for_Rumour_Detection_and_Veracity_Classification/6392078)

- [CREDBANK Dataset](http://compsocial.github.io/CREDBANK-data/)

## BS Detector

**BS Detector** : From a non-research related perspective, it is interesting to cite BS Detector, developed by Kaggle. It is a web crawler with knowledge about fake news websites, that has been used to build a dataset by monitoring such websites
for a period of time. The main issue is that it cannot be considered a gold standard since it is not annotated by humans.

This dataset is collected from a browser extension called BS detector developed for checking news veracity. It searches all links on a given web page for references to unreliable sources by checking against a manually compiled list of domains. The labels are the outputs of the BS detector, rather than human annotators.

**Reference** :

- [Github - bs-detector/bs-detector](https://github.com/bs-detector/bs-detector)
- [Github - selfagency/bs-detector](https://github.com/selfagency/bs-detector)

## Politifact

Politifact : PolitiFact – is a six-dimensional rating system developed to
check facts. It is frequently used to rate the accuracy and credibility of claims made by US officials and others (Roy, 2013).

The PolitiFact system largely depends on human intervention, during which, journalists assess information via watching TV, scanning social media, and evaluating reader comments.

**Reference** :

## Fake News Challenge dataset

Fake News Challenge dataset: This data is collected from a variety of sources and Twitter accounts. It contains around 50000 claim document pairs as training data with an imbalanced distribution over stance labels.

**Reference :**

- [kaggle.com/c/fake-news/data](https://www.kaggle.com/c/fake-news/data)

## Fact Extraction and verification (FEVER) dataset

**Fact Extraction and verification (FEVER) dataset**: This dataset is collected from Wikipedia and contains around 1,45,000 claim-document pairs as training data with imbalanced distribution over stance labels of 55, which is used as source data

Each statement is labeled as Supported, Refuted, or Not Enough Info. They also marked which sentences from Wikipedia they use as evidence. Fever makes it possible to develop a system that can predict the truthfulness of a claim together with the evidence, even though the type of facts and evidence from Wikipedia may still exhibit some major stylistic differences from those in real-world political campaigns.

**Reference :**

- [fever.ai/resources.html](https://fever.ai/resources.html)

- [Github - j6mes/fever2-sample](https://github.com/j6mes/fever2-sample) (updated)

- [Github - sheffieldnlp/fever-naacl-2018](https://github.com/sheffieldnlp/fever-naacl-2018) ( outdated )

## Fake news dataset

Kaggle fake news dataset : Fake news dataset

    - Fake.csv
    - True.csv

**Reference :**

- [kaggle.com/clmentbisaillon/fake-and-real-news-dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

## FakeNewsNet dataset

There are several datasets for fake news detection predicting whether the entire article is true or fake. For example, FAKENEWSNET is an ongoing data collection project for fake news research. It consists of headlines and body texts of fake news articles based on BuzzFeed and PolitiFact. It also collects information about the social engagements of these articles from Twitter.

**Reference :**

- **FakeNewsNet**: https://github.com/KaiDMML/FakeNewsNet

## ClaimBuster dataset

**Reference :** [ClaimBuster A Benchmark Dataset of Check-worthy Factual Claims](https://figshare.com/articles/dataset/ClaimBuster_A_Benchmark_Dataset_of_Check-worthy_Factual_Claims/11635293)

## SOME-LIKE-IT-HOAX

SOME-LIKE-IT-HOAX Consists of 15,500 posts from 32 Facebook pages, that is, the public profile of organizations (14 conspiracy and 18 scientific organizations).

This dataset is labeled based on the identity of the publisher instead of post-level annotations. A potential pitfall of such a dataset is that such kind of labeling strategies can result in machine learning models learning characteristics of each publisher, rather than that of the fake news.

**Reference :**

- [Github - gabll/some-like-it-hoax](https://github.com/gabll/some-like-it-hoax)

## MultiFC Dataset

Real-World Multi-Domain Dataset for Evidence-Based Fact Checking of Claims.

The MultiFC is the largest publicly available dataset of naturally occurring factual claims for the purpose of automatic claim verification. It is collected from 26 English fact-checking websites, paired with textual sources and rich metadata, and labeled for veracity by human expert journalists. In the figure below you can see one example of a claim instance. Entities are obtained via entity linking. Article and outlink texts, evidence search snippets and pages are not shown.

<p align="center"><img src="https://i.ibb.co/Bf1chmd/example.jpg" width="50%"></p>

**Reference :**

- [MultiFC Dataset](https://competitions.codalab.org/competitions/21163)

- [copenlu.github.io/publication/2019_emnlp_augenstein](https://copenlu.github.io/publication/2019_emnlp_augenstein/)

## ISOT Fake News Dataset

The dataset contains two types of articles fake and real News. This dataset was collected from real world sources; the truthful articles were obtained by crawling articles from Reuters.com (News
website). As for the fake news articles, they were collected from different sources.

The fake news articles were collected from unreliable websites that were flagged by Politifact (a fact-checking organization in the USA) and Wikipedia. The dataset contains different types of articles on different
topics, however, the majority of articles focus on political and World news topics.

The dataset consists of two CSV files. The first file named **“True.csv”** contains more than 12,600
articles from reuter.com. The second file named **“Fake.csv”** contains more than 12,600 articles from
different fake news outlet resources. Each article contains the following information: article title, text,
type and the date the article was published on. To match the fake news data collected for kaggle.com,
we focused mostly on collecting articles from 2016 to 2017. The data collected were cleaned and
processed, however, the punctuations and mistakes that existed in the fake news were kept in the text.

**Reference :**

- **Dataset** : [Fake News Detection Datasets - University of Victoria (uvic.ca)](https://www.uvic.ca/engineering/ece/isot/datasets/fake-news/index.php)

- **Documentation** : [ISOT Fake News Dataset ReadMe.pdf (uvic.ca)](https://www.uvic.ca/engineering/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf)

## Constraint@AAAI2021 - COVID19 Fake News Detection in English

COVID19 Fake News Detection in English - This subtask focuses on the detection of COVID19-related fake news in English. The sources of data are various social-media platforms such as Twitter, Facebook, Instagram, etc. Given a social media post, the objective of the shared task is to classify it into either fake or real news. For example, the following two posts belong to fake and real categories, respectively. 

**Reference**

- [Constraint-shared-task-2021](https://constraint-shared-task-2021.github.io/)

- Datasets released - COVID19 Fake News Detection in [Hindi](https://competitions.codalab.org/competitions/26654)

- Datasets released - COVID19 Fake News Detection in [English](https://competitions.codalab.org/competitions/26655)