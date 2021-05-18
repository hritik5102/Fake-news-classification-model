## Fake-news-classification-model &nbsp; ![](https://img.shields.io/github/forks/hritik5102/Fake-news-classification-model?style=social) ![](https://img.shields.io/github/stars/hritik5102/Fake-news-classification-model?style=social) ![](https://img.shields.io/github/watchers/hritik5102/Fake-news-classification-model?style=social) <br>

![](https://img.shields.io/github/repo-size/hritik5102/Fake-news-classification-model) ![](https://img.shields.io/github/license/hritik5102/Fake-news-classification-model?color=red) [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/hritik5102/Fake-news-classification-model) ![](https://img.shields.io/github/issues/hritik5102/Fake-news-classification-model?color=green) <br>
 ![](https://img.shields.io/github/issues-pr/hritik5102/Fake-news-classification-model?color=green) ![](https://img.shields.io/github/downloads/hritik5102/Fake-news-classification-model/total) ![](https://img.shields.io/github/last-commit/hritik5102/Fake-news-classification-model)
[![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square)](https://github.com/hritik5102/Fake-news-classification-model/blob/master/CONTRIBUTING.md)&nbsp;
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=flat-square)](https://www.paypal.me/AvsarJaiswal/100)&nbsp;

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

<div align="center" style="height:400px"> 
<img src="https://i.ibb.co/j5GJdrp/download.jpg" height="100%">
<h4><a href="http://www.posterfortomorrow.org/en/gallery/view/54205">Image source :- Protect Yourself from Fake News not just Corona Virus</a></h4>
</div>

<br/>

<!-- ALL-CONTRIBUTORS-BADGE:END -->
# Table of Contents
- [Table of Contents](#table-of-contents)
  - [News Cateogries](#news-cateogries)
  - [Architecture](#architecture)
  - [Presentation](#presentation)
  - [Demo-video](#demo-video)
  - [Tech stack](#tech-stack)
  - [Installation](#installation)
  - [Prerequisites](#prerequisites)
    - [How to run the app?](#how-to-run-the-app)
    - [How to stop the Deep learning model servers?](#how-to-stop-the-deep-learning-model-servers)
  - [Google colab notebook](#google-colab-notebook)
  - [Acknowledgement](#acknowledgement)
  - [Support me](#support-me)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
  - [Contributors](#contributors)

## News Cateogries

[(Back to Top)](#table-of-contents)

| No. |                 Content                 |                                                                                            Discription                                                                                            |
| :-: | :-------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|  1  |                 **Fake news**                  |                       `Fake News` - Sources that entirely fabricate information, disseminate deceptive content, or grossly distort actual news reports,aim of damaging the reputation of a person or entity, or making money through advertising revenue                       |
|  2  |                 **Satire**                  |                       `Satire` - Sources that use humor, irony, exaggeration, ridicule, and false information to comment on current events, providing fake insights about an on-going real news event.                       |
|  3  |               **Bias**                |                    `Extreme Bias` - Sources that come from a particular point of view and may rely on propaganda, decontextualized information, and opinions distorted as facts.                     |
|  4  |             **Conspiracy Theories**              |                 `Conspiracy Theory` - is an explanation or interpretation of events that is based on questionable or nonexistent evidence, which are almost always completely fabricated, even if individual elements of the theories contain nuggets of fact -- can be presented as fake news when they are packaged as factual news stories.                  |
|  5  |                 **Rumor**                 |                      `Rumor` - Sources that traffic in rumors, gossip, innuendo, and unverified claims, statement consisting of unverified pieces of information at the time of posting                      |
|  6  |                **State**                 |                     `State News` - Sources in repressive states operating under government sanction.                      |
|  7  |         **Junk science**          |            `Junk Science` - Sources that promote pseudoscience, metaphysics, naturalistic fallacies, and other scientifically dubious claims.             |
|  8  |        **Hate**        |           `Hate News` - Sources that actively promote racism (based on something such as religion, ethnicity, nationality, sexual orientation), misogyny, homophobia, and other forms of discrimination.            |
|  9  |               **Clickbait**               |                   `Clickbait` - Sources that provide generally credible content, but use exaggerated, misleading, or questionable headlines, social media descriptions, and/or images.                    |
| 10  |          **Unreliable**     |              `Unreliable` - Proceed With Caution, Sources that may be reliable but whose contents require further verification.               |
| 11  |            **Political**             |                `Political` - Sources that provide generally verifiable information in support of certain points of view or political orientations.                 |
| 12  |             **Reliable**              |                  `Credible` - Sources that circulate news and information in a manner consistent with traditional and ethical practices in journalism (Remember: even credible sources sometimes rely on clickbait-style headlines or occasionally make mistakes. No news organization is perfect, which is why a healthy news diet consists of multiple sources of information).                   |
| 13  |                **Celebrity**                 |                     `Celebrity` - Celebrity/Gossip magazines (sometimes referred to as tabloid magazines) are magazines that feature scandalous stories about the personal lives of celebrities and other well-known individuals.                     |
| 14  |          **Hoax**           |             `Hoax` - is a news containing facts that are either inaccurate or false but which are presented as genuine. A hoax news conveys a half-truth used deliberately to mislead the public.              |
| 15  |      **Unknown**      |        `Unknown` - is a sources that have not yet been analyzed (many of these were suggested by readers/users or are found on other lists and resources). Help us expand our resource by providing us information!        |
| 16  |                **Propaganda**                 |                     `Propaganda` - is the spreading of rumors, information which is often inaccurate and especially of a biased or misleading nature, used to promote a political cause or point of view.                      |
| 18  |               **Misinformation**               |                   `Misinformation` - is false, inaccurate, or misleading information that is communicated regardless of an intention to deceive. Examples of misinformation are false rumors, insults, and pranks.                    |
| 19  |            **Poor Sourcing**            |                `Poor Sourcing` - is the out-of-context information that does not on its own constitute fake news. This kind of information is not wholly fabricated, and it can exist within a news report that is based on actual events that occurred but does not have the proper evidence for it.                |
| 20  |                 **Lack of Transparency**                 |                      `Lack of Transparency` - is the out-of-context information that does not on its own constitute fake news. This kind of information is not wholly fabricated, and it can exist within a news report that is based on actual events that occurred but does not have the proper evidence for it.                      |
| 21  |                 **False Information**                  |                     `False Information` - Sources that entirely fabricate information, disseminate deceptive content, or grossly distort actual news reports,aim of damaging the reputation of a person or entity, or making money through advertising revenue                      |
| 22  |            **Sensationalism**            |                 `Sensationalism` - In journalism (and more specifically, the mass media), sensationalism is a type of editorial tactic. Events and topics in news stories are selected and worded to excite the greatest number of readers and viewers.                 |
| 23  |            **Plagarism**             |                `Plagiarism` is the representation of another author's language, thoughts, ideas, or expressions as one's own original work. Plagiarism is considered a violation of integrity and a breach of journalistic ethics.                 |

## Architecture 

[(Back to Top)](#table-of-contents)

<p align="center"><img src="https://i.ibb.co/bRkVN9p/Architecture.png" alt="Architecture" border="0" width="80%"></p>

## Presentation

[(Back to Top)](#table-of-contents)

Read the project presentation fron [here 📌](https://docs.google.com/presentation/d/1RUkxMFmhWDfAduH-eDqUx_FYHMIZCxXCQnImiL7Nx3A/edit?usp=sharing)
## Demo-video

[(Back to Top)](#table-of-contents)

[![Project Demo Video](https://yt-embed.herokuapp.com/embed?v=_j8sBhPnF6Y)](https://www.youtube.com/watch?v=_j8sBhPnF6Y "Project Demo Video")

## Tech stack 

[(Back to Top)](#table-of-contents)

1. **Programming Language** : Python
2. **Frontend** : streamlit
3. **Tools** : Colab notebook, VS Code
4. **Machine learning Library** : Tensorflow, PyTorch, Keras, Huggingface transformers, simpletransformers
5. **Web framework** : Flask
6. **Web server** : Nginx
7. **Web application/Model Deployment** : AWS EC2 Instance
   
## Installation 

[(Back to Top)](#table-of-contents)<br/>

**Clone git repository**

```sh
    $ git clone "https://github.com/hritik5102/Fake-news-classification-model"
```
## Prerequisites

[(Back to Top)](#table-of-contents)

Run the setup file on git bash or any linux terminal:

```sh
$ bash setup.sh
```

### How to run the app?

Run the following commands:
1. ```bash start-server.sh ``` on git bash or any linux terminal
This will start the deep learning model servers.

2. ```cd src```

3. ```streamlit run app.py```

### How to stop the Deep learning model servers?

run ```bash stop-server.sh``` on git bash or any linux terminal

## Google colab notebook

[(Back to Top)](#table-of-contents)

| Filename                                    | Notebook                                                                                                                                                                                                                                           |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GPT2 Model** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hritik5102/Fake-news-classification-model/blob/main/Models/GPT2_Model/notebook/GPT2_model.ipynb)      |
| **BiLSTM + GloVe Model**  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hritik5102/Fake-news-classification-model/blob/main/Models/Bidirectional_LSTM_Glove/notebook/Fake_News_Detection_GloVe.ipynb) |
| **BERT Model**                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hritik5102/Fake-news-classification-model/blob/main/Models/BERT_Fake_News_Classification/notebook/Bert_model.ipynb)                          |
| **Roberta Model**                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hritik5102/Fake-news-classification-model/blob/main/Models/Roberta_Model/notebook/Roberta_model.ipynb)                          |


## Acknowledgement 
[(Back to Top)](#table-of-contents)

Some resources have been used to build this project, so I'd like to acknowledge the resources in the [reference](reference.md) section. Take a look.

If you think that I've referred any piece of code or material but have not acknowledged it. Please create an issue mentioning the site info & a link pointing to that material.

## Support me

[(Back to Top)](#table-of-contents)

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/hritikdj)

<!-- ROADMAP -->
## Roadmap

[(Back to Top)](#table-of-contents)

See the [open issues](https://github.com/hritik5102/Fake-news-classification-model/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

[(Back to Top)](#table-of-contents)

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Make sure your changes don't break existing functionality without `good reason`.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


Discuss the features, ideas you want to add to the project from [here 📌](https://github.com/hritik5102/Fake-news-classification-model/discussions)
## License

[(Back to Top)](#table-of-contents)

Distributed under the [MIT License](LICENSE). See LICENSE for more information.

## Contact

[(Back to Top)](#table-of-contents)

| No. | Name               |                                                      Twitter handle 🐦 | Email 📩 |
| :-: | :-------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----: |
|1. | Heet sakaria |[@HeetSakaria](https://twitter.com/HeetSakaria)|[heet.sakaria@somaiya.edu](mailto:heet.sakaria@somaiya.edu)|
|2. | Hritik Jaiswal |[@imhritik_dj](https://twitter.com/imhritik_dj)|[hritik.jaiswal@somaiya.edu](mailto:hritik.jaiswal@somaiya.edu)|



**Project Link** - [hritik5102/Fake-news-classification-model (github.com)](https://github.com/hritik5102/Fake-news-classification-model)

## Contributors

[(Back to Top)](#table-of-contents)

Thanks goes to these wonderful people 👏👏

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/heet9022"><img src="https://avatars0.githubusercontent.com/u/41733742?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Heet Sakaria</b></sub></a><br /><a href="https://github.com/hritik5102/Fake-news-classification-model/commits?author=heet9022" title="Code">💻</a> <a href="#ideas-heet9022" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/vedangparasnis"><img src="https://avatars2.githubusercontent.com/u/35874709?v=4" width="100px;" alt=""/><br /><sub><b>vedangparasnis</b></sub></a><br /><a href="https://github.com/hritik5102/Fake-news-classification-model/commits?author=vedangparasnis" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

```bash
 _____ _                 _     __   __            
|_   _| |               | |    \ \ / /            
  | | | |__   __ _ _ __ | | __  \ V /___  _   _   
  | | | '_ \ / _` | '_ \| |/ /   \ // _ \| | | |  
  | | | | | | (_| | | | |   <    | | (_) | |_| |  
  \_/ |_| |_|\__,_|_| |_|_|\_\   \_/\___/ \__,_| 
```
</p>

[(Back to Top)](#table-of-contents)

