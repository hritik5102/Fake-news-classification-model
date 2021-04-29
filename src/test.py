# import csv
# import os
# from url_utils import get_domain, format_url, get_data_path
# import json
# import urllib.parse
# import pandas as pd
# import io
# import requests
# import bs4
# from bs4 import BeautifulSoup

# with open(get_data_path('fake_news_sites.json')) as json_file:
#     fake_news_db_news = json.load(json_file)

# with open('src/json_local/categories.json') as json_file:
#     categories = json.load(json_file)

# with open('src/json_local/opensources/sources.json') as json_file:
#     open_source_json = json.load(json_file)

# # domain_name = get_domain(
# #     'https://www.washingtonpost.com/politics/2021/04/01/matt-gaetzs-claim-that-travel-records-debunk-allegations-against-him/')

# # formated_domain = format_url(domain_name)
# # print("Domain name : ", domain_name)
# # print("Format URL : ", format_url(domain_name))
# # print(len(fake_news_db_news))


# # def get_fb_news_data(domain_name, formated_domain, fake_news_db_news):
# #     for i in range(len(fake_news_db_news)):
# #         if fake_news_db_news[i]["siteUrl"] == formated_domain or fake_news_db_news[i]["siteUrl"] == domain_name:
# #             return fake_news_db_news[i]

# #     return "URL is not found in Fake News Site Database"


# # def get_opensource_news(domain_name, open_source_json):
# #     try:
# #         source_info = open_source_json[domain_name]
# #     except KeyError:
# #         source_info = "URL is not found in OpenSource Database"
# #     return source_info


# # res = get_fb_news_data(domain_name, formated_domain, fake_news_db_news)

# # print("Site URL : ", res)
# # try:
# #     print(categories[res["siteCategory"]])
# # except TypeError:
# #     print("siteCategory is matching with domain")

# # res1 = get_opensource_news(domain_name, open_source_json)
# # print(res1)

# # dir_path = os.path.dirname(os.path.realpath(__file__))
# # print(dir_path)

# # import streamlit as st

# # x = ["Banana", "Apple", "Orange", "Pear", "Nectarine"]

# # # for i in x:
# # #     st.markdown(
# # #         f'<span style="background-color:#00C4EB;border-radius:5px;box-shadow: 0 5px 0 rgb(0, 116, 191);color: #FFFFFF;padding: 0.5em 1em;position: relative;text-decoration: none;font-weight:bold;cursor: pointer;">{i}</span>', unsafe_allow_html=True)
# # length = len(x)
# # if x:
# #     for i in range(length):
# #         cols = st.beta_columns(length)
# #         cols[i].markdown(
# #             f'<span style="background-color:#00C4EB;border-radius:5px;box-shadow: 0 5px 0 rgb(0, 116, 191);color: #FFFFFF;padding: 0.5em 1em;font-weight:bold;cursor: pointer">{x[i]}</span>', unsafe_allow_html=True)


# # print(__file__)
# # print(os.path.realpath(__file__))
# # print(os.path.dirname(os.path.realpath(__file__)))
# # print(os.getcwd())

# filePath = os.path.dirname(os.path.realpath(__file__)) + '/Fake_news_site.csv'
# data = pd.read_csv(filePath)

# data = data.rename(columns={'Site name': 'site_name',
#                    'Type of site': 'type_of_site', 'Registration': 'author'})
# # print(data.head())

# site_list = data['site_name'].values.tolist()

# # duplicate = data[data.duplicated(keep='first')]
# # print(duplicate)

# fake_news_site_list = [fake_news_db_news[i]["siteUrl"]
#                        for i in range(len(fake_news_db_news))]
# # print(type(fake_news_db_news))
# # print(len(fake_news_db_news))
# # [fake_news_site_list[i]["siteTitle"] for i in range(len(fake_news_db_news))]
# # fake_news_site_list.append()

# print(type(site_list[:5]))
# print(site_list[:5])
# print(fake_news_site_list[:5])


# fn_news_domain_list = []
# # print(parsed_url)
# for i in fake_news_site_list:
#     parsed_url = urllib.parse.urlparse(i)
#     if parsed_url.netloc == '':
#         fn_news_domain_list.append(parsed_url.path)
#     else:
#         fn_news_domain_list.append(parsed_url.netloc)

# # fn_news_domain_list = [get_domain(i) for i in fake_news_site_list]
# print(fn_news_domain_list[:5])

# print("Match found between FB_NEWS vs Excel", set(
#     site_list).intersection(fn_news_domain_list))

# open_source_site_list = list(open_source_json.keys())
# print(open_source_site_list[:5])
# print("Match found between Opensource vs Excel", set(
#     site_list).intersection(open_source_site_list))

# # Zero Hedge

# # data_dict = data.to_dict()
# # print(data_dict)

# print(data.shape[0])

# # data_dict = {}

# print(type(fake_news_db_news))
# # if type(fake_news_db_news) is dict:
# #     fake_news_db_news = [fake_news_db_news]

# data_list = []  # fake news
# data_dict = {}  # opensource

# # for i in range(data.shape[0]):
# #     # data_dict["siteTitle"] = ''
# #     # data_dict["siteCategory"] = data['type_of_site'][i]
# #     # data_dict["siteUrl"]: data['site_name'][i]
# #     # data_dict["siteGoogleHits"]: ''
# #     # data_dict["siteFacebookLikes"]: ''
# #     # data_dict["siteTwitterFollowers"]: ''
# #     # data_dict["sitePoliticalAlignment"]: ''
# #     # data_dict["siteNotes"]: ''

# #     # data_json = json.load(get_data_path('fake_news_sites.json'))
# #     data_list.append({
# #         "siteTitle": '',
# #         "siteCategory": data['type_of_site'][i],
# #         "siteUrl": data['site_name'][i],
# #         "siteGoogleHits": '',
# #         "siteFacebookLikes": '',
# #         "siteTwitterFollowers": '',
# #         "sitePoliticalAlignment": '',
# #         "siteNotes": ''
# #     })

# # print(data_list)
# # with open(get_data_path('fake_news_sites.json'), 'a') as outfile:
# #     json.dump(data_list, outfile)

# # for i in range(data.shape[0]):
# #     data_dict[data['site_name'][i]] = {
# #         "type": data['type_of_site'][i],
# #         "2nd type": "",
# #         "3rd type": "",
# #         "Source Notes (things to know?)": ""
# #     }

# # print(data_dict)
# # with open(get_data_path('opensources/sources.json'), 'a') as outfile:
# #     json.dump(data_dict, outfile)


# def get_text(url):
#     try:
#         result = requests.get(str(url))
#     except Exception:
#         print("error in scraping url")
#         return None
#     src = result.content
#     soup = BeautifulSoup(src, 'lxml')
#     test_text = []
#     with io.open('output.txt', 'w', encoding='utf8') as f:
#         for header in soup.find_all(['a']):
#             test_text.append(header.get_text())
#             f.write(header.get_text() + u'\n')
#             # for elem in header.next_siblings:
#             #     if elem.name and elem.name.startswith('h'):
#             #         # stop at next header
#             #         break
#             #     if elem.name == 'p':
#             #         f.write(elem.get_text() + u'\n')
#     return test_text

# # print(get_text('https://mediabiasfactcheck.com/fake-news/'))


# # output_file = open('output.txt', "r", "UTF8")
# # content = output_file.read()
# content = open('output.txt', 'r', encoding="utf8").readlines()
# # print(content)

# # content_list = content.split('\n')
# # print(content_list)
# # site_title, site_link, site_categories, site_notes = [], [], [], []

# for i in content:
#     try:
#         site_title, site_link, site_categories, site_notes = i.split('|')
#         # print(site_title, site_link, site_categories, site_notes)
#         if site_link not in open_source_site_list:
#             # data_list.append({
#             #     "siteTitle": site_title,
#             #     "siteCategory": [i for i in site_categories.split(', ')],
#             #     "siteUrl": site_link,
#             #     "siteNotes": site_notes
#             # })
#             category = [i for i in site_categories.split(', ')]
#             category_length = len(category)
#             if category_length == 1:
#                 data_dict[site_link] = {
#                     "type": category[0],
#                     "2nd type": "",
#                     "3rd type": "",
#                     "Source Notes (things to know?)": site_notes
#                 }
#             elif category_length == 2:
#                 data_dict[site_link] = {
#                     "type": category[1],
#                     "2nd type": category[0],
#                     "3rd type": "",
#                     "Source Notes (things to know?)": site_notes
#                 }
#             else:
#                 data_dict[site_link] = {
#                     "type": category[1],
#                     "2nd type": category[0],
#                     "3rd type": category[2],
#                     "Source Notes (things to know?)": site_notes
#                 }
#     except Exception as ec:
#         print(ec, i)

#     # if len(x) != 0:
#     # try:
# # 8381
#     # })        except Exception as ec:
#     #         print(i)
# # with open(get_data_path('fake_news_sites.json'), 'a') as outfile:
# #     json.dump(data_list, outfile)
# with open(get_data_path('opensources/sources.json'), 'a') as outfile:
#     json.dump(data_dict, outfile)
# # print(data_list[:4])
# # # print("2nd Amendment Daily News (secondamendmentdaily.com)".split('('))
# # print(site_title[:5], site_link[:5], site_categories[:5])
# # print("Opensource : ", len(set(site_link).intersection(open_source_site_list)))
# # print("FB NEWS : ", len(set(site_link).intersection(fn_news_domain_list)))

# # print("Opensource not maching: ", len(
# #     set(site_link).difference(open_source_site_list)))
# # print("FB NEWS not maching: ", len(
# #     set(site_link).difference(fn_news_domain_list)))


# # 2312

# # data_dict = {}
# # for i,j in zip(site_title,site_link):
# #     if i in open_source_site_list:
# #         continue
# #     else:
# #             data_dict[data['site_name'][i]] = {
# #         "type": data['type_of_site'][i],
# #         "2nd type": "",
# #         "3rd type": "",
# #         "Source Notes (things to know?)": ""
# #     }

from ..classification import LGB
print("runnning LGB model")
sample = "Donald Trump was born in Pakistan as Dawood Ibrahim Khan New Delhi: A video has gone viral showing a Pakistani anchor claiming that US President-elect Donald Trump was born in Pakistan and not in the United States of America.  The report further alleged that Trump's original name is Dawood Ibrahim Khan. In the video, the Neo News anchor elaborated on Trump's journey from North Waziristan to England and then finally to Queens, New York.  Neo news had cited tweets and a picture on social media to back its claim. The video was broadcast last month but went viral after Trump’s election victory on November 8."
lgb = LGB()
if lgb.predict(sample):
    print("News article is REAL")
else:
    print("News article is FAKE")
