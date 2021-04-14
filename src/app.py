# To save your changes, copy your custom theme into the clipboard and paste it into the[theme] section of your .streamlit/config.toml file.
# [theme]
# primaryColor="#f63366"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#f0f2f6"
# textColor="#262730"
# font="sans serif"

import os
import json
import nltk
import datetime
import newspaper
import numpy as np
import streamlit as st
from time import sleep
from newspaper import Article, news_pool
from urllib.parse import urlparse, ParseResult
from url_utils import get_domain, format_url, get_data_path
from newspaper.article import ArticleException, ArticleDownloadState

# Download
nltk.download('punkt')

st.set_page_config(
    layout="wide", page_title='Fake news detection', page_icon="🤗")


def main_page():
    html_temp = """
    <div style="background-color:#02203c;padding:10px">
    <h2 style="color:white;text-align:center;font-weight:bold">Fake news site information</h2>
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


def home_page():
    """
    Scrape and parse textual content from web resource. This method employs Article from Newspaper3k library to download and parse html from the web resource. It uses heuristics to scrape main body of visible text.
    :param url: Uniform Resource Locator.
    :return: Scraped content of web resource.
    """
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

    # site_with_articles = newspaper.build(user_input, memoize_articles=False)
    # site_with_articles.print_summary()
    # left, right = st.beta_columns((1, 2))
    # name = ["Author", "Date", "Title", "Text", "Top Images",
    #         "Movies", "Related tags", "Keywords (NLP)", "Summary (NLP)"]

    # article_info = [my_article.authors, my_article.publish_date, my_article.title, my_article.text,
    #                  my_article.top_image, my_article.movies, my_article.tags]

    # if st.button('Generate Text'):
    #     st.markdown('''---''')
    #     with left:
    #         left.markdown('''**Content**''', unsafe_allow_html=True)
    #         for i in name:
    #             left.write(i)

    #     with right:
    #         right.markdown('''**Discription**''', unsafe_allow_html=True)
    #         for i in article_info:
    #             right.write(i)

    if st.button('Check authenticity'):
        st.header("News site authencity")
        st.markdown('''---''')
        left, right = st.beta_columns((1, 2))

        # st.markdown(f'''<table><tr>
        #             <td>Summary (NLP)</td>
        #             <td>{nlp_summary}</td>
        #         </tr></table>''', unsafe_allow_html=True)

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
            # st.markdown(
            #     f'''<div style="display: block;text-align:center"><img src={image_url}></div><br>''', unsafe_allow_html=True)
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
            st.video(videos)
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
        # length = len(nlp_keywords)
        if nlp_keywords:
            st.info(nlp_keywords)
            # for i in range(length):
            #     cols = st.beta_columns(length)

            # for i in range(length):
            #     cols[i].markdown(
            #         f'<span style="background-color:#00C4EB;border-radius:5px;box-shadow: 0 5px 0 rgb(0, 116, 191);color: #FFFFFF;padding: 0.4em 0.8em;font-weight:bold;cursor: pointer">{nlp_keywords[i]}</span>', unsafe_allow_html=True)
            # st.success(nlp_keywords)
        else:
            st.warning(
                "Coudn\'t able to get the top keywords or Invalid URL Provided")

        st.markdown('''### **Summary (NLP)**''')
        nlp_summary = my_article.summary
        if nlp_summary:
            st.markdown(f'{nlp_summary}', unsafe_allow_html=True)
        else:
            st.warning(
                "Coudn\'t able to get the top keywords or Invalid URL Provided")

        # st.markdown(f'''<table><tr>
        #             <td>Summary (NLP)</td>
        #             <td>{nlp_summary}</td>
        #         </tr></table>''', unsafe_allow_html=True)

        # if st.button('Generate Text'):
        #     st.markdown(f'''
        #                 <table class="table">
        #                 <tbody>
        #                 <tr>
        #                     <td>Title</td>
        #                     <td>{ my_article.title }</td>
        #                 </tr>
        #                 <tr>
        #                     <td>Authors</td>
        #                     <td>{ my_article.authors }</td>
        #                 </tr>
        #                 <tr>
        #                     <td>Text</td>
        #                     <td>{ my_article.text }</td>
        #                 </tr>
        #                 <tr>
        #                     <td>Top Image</td>
        #                     <td>
        #                         <img src="{ my_article.top_image }"/>
        #                     </td>
        #                 </tr>
        #                 <tr>
        #                     <td>Movies (Videos)</td>
        #                     <td>{ my_article.movies }</td>
        #                 </tr>
        #                 <tr>
        #                     <td>Keywords (NLP)</td>
        #                     <td>{ my_article.keywords }</td>
        #                 </tr>
        #                 <tr>
        #                     <td>Summary (NLP)</td>
        #                     <td>{ my_article.summary }</td>
        #                 </tr>
        #                 <tr>
        #                     <td>my_article HTML</td>
        #                     <td>
        #             <pre>
        #                 <code class="language-markup">
        #                 { my_article.html }
        #                 </code>
        #             </pre>
        #                     </td>
        #                 </tr>
        #                 </tbody>
        #             </table>
        #     ''', unsafe_allow_html=True)


main_page()
# http://www.ancient-code.com/did-ancient-mankind-know-the-secrets-of-levitation/
# https://www.washingtonpost.com/politics/2021/04/01/matt-gaetzs-claim-that-travel-records-debunk-allegations-against-him/
# https://21stcenturywire.com/2021/04/07/texas-governor-signs-order-banning-use-of-vaccine-passports/
# https://www.secondamendmentdaily.com/2021/03/chuck-schumer-says-that-law-abiding-licensed-firearms-dealers-are-evil-and-so-are-ghost-guns/
# https://www.hindustantimes.com/india-news/cbse-class-10-exams-cancelled-class-12-exams-postponed-says-govt-after-pm-modi-s-covid-review-meet-101618383590781.html
