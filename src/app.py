import os
import json
import nltk
import requests
import numpy as np
import streamlit as st
from time import sleep
from newspaper import Article
from urllib.parse import urlparse, ParseResult
from url_utils import get_domain, format_url, get_data_path
from newspaper.article import ArticleException, ArticleDownloadState
import model_service
import asyncio
import vt

# Download if does not exists
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    import nltk

st.set_page_config(
    layout="wide", page_title='Fake news detection', page_icon="🤗")


def main_page():
    html_temp = """
    <div style="background-color:#02203c;padding:10px">
    <h2 style="color:white;text-align:center;font-weight:bold">Fake vs Fact News</h2>
    </div>
    <hr/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image("./assets/images/fake-news.png")
    st.sidebar.image(
        "./assets/images/guy_with_laptop.jpg",
        width=300,
    )
    menu = ["Home", "Log In", "Sign Up", "Learn"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == menu[0]:
        home_page()


def get_fb_news_data(domain_name, formated_domain, fake_news_db_news):
    '''
    Input : Domain name with Top level domain (eg bbc.com), Formatted Domain 
    Output : Information stored in JSON File (Category, URL, Source Notes)
    '''
    for i in range(len(fake_news_db_news)):
        if fake_news_db_news[i]["siteUrl"] == formated_domain or fake_news_db_news[i]["siteUrl"] == domain_name:
            return fake_news_db_news[i]

    return None


def get_opensource_news(domain_name, formated_domain, open_source_json):
    '''
    Input : Domain name with Top level domain (eg bbc.com), Formatted Domain 
    Output : Information stored in JSON File (Category, URL, Source Notes)
    '''
    # Multiple try - except block : https://stackoverflow.com/questions/17322208/multiple-try-codes-in-one-block
    try:
        source_info = open_source_json[domain_name]
    except KeyError:
        try:
            source_info = open_source_json[formated_domain]
        except KeyError:
            source_info = None
    return source_info

def scan_url(user_input):
    client = vt.Client(os.environ.get('VIRUS_TOTAL_API_KEY'))
    try:
        analysis = client.scan_url(user_input, wait_for_completion=True)
        result =  analysis.to_dict()
        client.close()
        return result['attributes']['results']
    except Exception as ec:
        print(ec)
        
def home_page():

    # Scrape and parse textual content from web resource. This method employs Article from Newspaper3k library to download and parse html from the web resource. It uses heuristics to scrape main body of visible text.
    # :param url: Uniform Resource Locator.
    # :return: Scraped content of web resource.

    user_input = st.text_input('Enter URL of an article or text')

    with open(get_data_path('fake_news_sites.json')) as json_file:
        fake_news_db_news = json.load(json_file)

    with open(get_data_path('categories.json')) as json_file:
        categories = json.load(json_file)

    with open(get_data_path('opensources/sources.json')) as json_file:
        open_source_json = json.load(json_file)

    try:
        # Get domain name from the url
        domain_name = get_domain(user_input)

        # Get formated domain
        formated_domain = format_url(domain_name)

    except Exception:
        st.warning("Enter an URL to suppress the warning !!")

    try:
        my_article = Article(user_input, language="en", keep_article_html=True)
        my_article.download()
        slept = 0
        while my_article.download_state == ArticleDownloadState.NOT_STARTED:
            # Raise exception if article download state does not change after 10 seconds
            if slept > 9:
                raise ArticleException('Download never started')
            sleep(1)
            slept += 1
        my_article.parse()
    except Exception as ec:
        print(ec)

    if st.button('Check authenticity'):
        st.header("VirusTotal - Malicious URL Scanner (virustotal.com)")
        st.markdown('''---''')
        with st.spinner(text="Fetching measures - Analysis in progress"):
            # task = asyncio.create_task(scan_url(user_input))
            # json_data = await task
            json_data = scan_url(user_input=user_input)
            if json_data is not None:
                category_key = list(json_data.keys())
                category_value = [json_data[i]['result'] for i in category_key]
                left, center, right = st.beta_columns((1, 2, 1))

                with left:
                    left.markdown('''**No.** ''', unsafe_allow_html=True)
                    for i in range(1, 21):
                        left.write(i)
                with center:
                    center.markdown('''**Detected by**''',unsafe_allow_html=True)
                    for i in category_key[:20]:
                        center.write(i)
                with right:
                    right.markdown('''**Result**''',unsafe_allow_html=True)
                    for link in category_value[:20]:
                        if link == 'clean':
                            right.markdown(f'<span style="color:green">clean site</span>', unsafe_allow_html=True)
                        else:
                            right.markdown(f'<span style="color:red">{link}</span>', unsafe_allow_html=True)
            else:
                st.warning("Couldn't able to get detect the site or Invalid URL provided !!")

        st.header("News site authencity")
        st.markdown('''---''')

        left, right = st.beta_columns((1, 2))
        res = get_opensource_news(
            domain_name, formated_domain, open_source_json)
        left.markdown(
            '''**Source** : OpenSource http://www.opensources.co/''', unsafe_allow_html=True)
        right.markdown(
            f'**Checking Domain** : {domain_name}', unsafe_allow_html=True)
        if res is None:
            right.warning("URL is not found in OpenSource Database")
        else:
            right.markdown(
                f'**Category** : {res["type"]}', unsafe_allow_html=True)
            try:
                right.markdown(
                    f'**Discription** : {categories[res["type"]]}', unsafe_allow_html=True)
            except:
                right.warning("Category Discription isn't available !!")
            if res["Source Notes (things to know?)"]:
                right.markdown(
                    f'**Source Notes (things to know?)** : {res["Source Notes (things to know?)"]}', unsafe_allow_html=True)

        st.markdown('''---''')
        left1, right1 = st.beta_columns((1, 2))
        res1 = get_fb_news_data(
            domain_name, formated_domain, fake_news_db_news)

        left1.markdown('''**Source** : FakeNews Site DB''',
                       unsafe_allow_html=True)
        right1.markdown(
            f'**Checking Domain** : {domain_name}', unsafe_allow_html=True)
        if res1 is None:
            right1.warning("URL is not found in Fake news site database")
        else:
            try:
                right1.markdown(
                    f'**Category** : {res1["siteCategory"]}', unsafe_allow_html=True)
                right1.markdown(
                    f'**Site name** : {res1["siteTitle"]}', unsafe_allow_html=True)
                if type(res1["siteCategory"]) is list:
                    right1.markdown(
                        f'**Discription** : {categories[res1["siteCategory"][0]]}', unsafe_allow_html=True)
                else:
                    right1.markdown(
                        f'**Discription** : {categories[res1["siteCategory"]]}', unsafe_allow_html=True)

                if res1["siteNotes"]:
                    right1.markdown(
                        f'**Source Notes (things to know?)** : {res1["siteNotes"]}', unsafe_allow_html=True)
            except Exception:
                st.warning("Category is not available for this site !!")

            if res1["siteCategory"] == 'reliable':
                st.success("This is a trusted news site, which means the claim and article published on this site is transparent, authentic, trustworthy, complete, and in the absence of biases, it also protects audiences and users from disinformation.")
            else:
                st.error(
                    "This news site is not reliable or not authentic, the information published by this site might not be true !!")

        st.markdown('''### **Article Title**''')
        # st.header(Article Title)
        title = my_article.title
        if title:
            st.markdown(f'{title}')
        else:
            st.warning(
                "Coudn\'t able extract the title or Invalid URL Provided")

        st.markdown('''### **Article Authors **''')
        author = my_article.authors
        if len(author) != 0:
            # st.markdown(f'{author}')
            st.markdown(
                f'<span style="background-color:#00C4EB;border-radius:5px;box-shadow: 0 5px 0 rgb(0, 116, 191);color: #FFFFFF;padding: 0.5em 1em;position: relative;text-decoration: none;font-weight:bold;cursor: pointer;">{author[0]}</span>', unsafe_allow_html=True)
        else:
            st.warning(
                "Coudn\'t able extract the author name or Invalid URL Provided")

        st.markdown('''### **Publish Date**''')
        date = my_article.publish_date
        if date:
            st.info(f'{date} ')
        else:
            st.warning(
                "Coudn\'t able extract the publish date or Invalid URL Provided")

        st.markdown('''### **Image**''')
        image_url = my_article.top_image
        if image_url:
            st.image(image_url, caption="Article Top Image")
            st.markdown(
                f'''<p align="center"><b> Source URL : <b><a href="{ image_url }">{ image_url }</a></p>''', unsafe_allow_html=True)
        else:
            st.warning(
                "Coudn\'t able extract the Image or Invalid URL Provided or No image is present")

        st.markdown('''### **Article Text**''')
        article_text = my_article.text
        if article_text:
            with st.beta_expander("🧙 Click here for more info about the article 🔮"):
                st.markdown(f'{article_text}', unsafe_allow_html=True)
        else:
            st.warning(
                "Coudn\'t able extract the publish article or Invalid URL Provided")

        st.markdown('''### **Movies / Videos**''')
        videos = my_article.movies
        if videos:
            st.video(videos[0])
        else:
            st.warning(
                "Coudn\'t able extract the publish videos or No videos were published or Invalid URL Provided ")

        try:
            my_article.nlp()
        except Exception as ec:
            st.error(ec)
        # except ArticleException:
        #     st.error("Article Exception Occured !!")

        st.markdown('''### **Keywords (NLP)**''')
        nlp_keywords = my_article.keywords
        if nlp_keywords:
            st.info(nlp_keywords)
        else:
            st.warning(
                "Coudn\'t able to get the top keywords or Invalid URL Provided")

        st.markdown('''### **Summary (NLP)**''')
        nlp_summary = my_article.summary
        if nlp_summary:
            st.markdown(f'{nlp_summary}', unsafe_allow_html=True)
        else:
            st.warning(
                "Coudn\'t able to get the summary of the article or Invalid URL Provided")

        st.header("News article veracity")
        st.markdown('''---''')

        if article_text is not None:
            
            with st.spinner(text="Inference is in Progress ⏳ ..."):
                output_label = asyncio.run(model_service.predict_from_server(article_text))
                # left,right = st.beta_columns((1,2))
                st.markdown('''**Analysis based on:** : Artificial intelligence''')
                st.markdown('''**Notes:** WARNING: This result may be inaccurate! This domain wasn't categorised on any human maintained list thus analysis was performed by machine learning model.''')
                if output_label:
                    st.markdown(
                        f'Predicted label : {output_label}', unsafe_allow_html=True)
                    st.success("Real news")
                else:
                    st.markdown(
                        f'Predicted label : {output_label}', unsafe_allow_html=True)
                    st.error("Fake news")
            st.balloons()     
        else:
            st.warning("Article text is not found, hence news article veracity analysis is incomplete !!")

            # right.markdown('''Artificial intelligence''')


main_page()
# http://www.ancient-code.com/did-ancient-mankind-know-the-secrets-of-levitation/
# https://www.washingtonpost.com/politics/2021/04/01/matt-gaetzs-claim-that-travel-records-debunk-allegations-against-him/
# https://21stcenturywire.com/2021/04/07/texas-governor-signs-order-banning-use-of-vaccine-passports/
# https://www.secondamendmentdaily.com/2021/03/chuck-schumer-says-that-law-abiding-licensed-firearms-dealers-are-evil-and-so-are-ghost-guns/
# https://www.hindustantimes.com/india-news/cbse-class-10-exams-cancelled-class-12-exams-postponed-says-govt-after-pm-modi-s-covid-review-meet-101618383590781.html
# https://indianexpress.com/article/india/pm-narendra-modi-address-to-nation-live-update-7281920/
# https://english.newsnationtv.com/world/news/donald-trump-born-in-pakistan-his-real-name-is-dawood-ibrahim-khan-claims-pak-media-150693.html
