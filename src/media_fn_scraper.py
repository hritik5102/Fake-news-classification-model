import io
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from url_utils import get_data_path
import json


def get_text(url):
    try:
        result = requests.get(str(url))
    except Exception:
        print("error in scraping url")
        return None
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    test_text = []
    with io.open('output.txt', 'w', encoding='utf8') as f:
        for header in soup.find_all(['a']):
            test_text.append(header.get_text())
            f.write(header.get_text() + u'\n')
    return test_text


def get_url(url):
    try:
        result = requests.get(str(url))
    except Exception:
        print("error in scraping url")
        return None
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    with io.open('output_links_page.txt', 'w', encoding='utf8') as f:
        for header in soup.find_all('a', href=True):
            f.write('https://mediabiasfactcheck.com' + header['href'] + u'\n')


# get_url("https://mediabiasfactcheck.com/fake-news")


def get_categories(url):
    try:
        result = requests.get(str(url))
    except Exception:
        print("error in scraping url")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    with io.open('output_category.txt', 'a', encoding='utf8') as f:
        f.write(u'\n' + url + u'\n' + '='*100 + u'\n')
        try:
            for header in soup.find_all(['strong']):
                f.write(header.get_text() + u'\n')
        except Exception:
            f.write(u'\n' + "Unable to scrape information" + u'\n')


def get_fn_categories():
    output_file = open('output_links_page.txt', 'r').readlines()
    output_list = [line.strip() for line in output_file]
    for i in output_list[344:]:
        get_categories(i)


def get_data_csv():

    filePath = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'fake_news_list.csv')

    data = pd.read_csv(filePath)
    # print(data.head())
    data = data.replace({'conspiracy': 'Conspiracy Theories', 'fake': 'False Information',
                         'junksci': 'junk science', 'unknown': 'Unknown'})

    # Because after 917 row - site is repeated in fake_news_list.csv
    site_list = data['site_name'].values.tolist()[:916]
    type1 = data['type1'].values.tolist()[:916]
    type2 = data['type2'].values.tolist()[:916]
    type3 = data['type3'].values.tolist()[:916]

    return site_list, type1, type2, type3


def get_data_json():
    with open(get_data_path('fake_news_sites.json')) as json_file:
        fake_news_db_news = json.load(json_file)

    with open(get_data_path('categories.json')) as json_file:
        categories = json.load(json_file)

    with open(get_data_path('opensources/sources.json')) as json_file:
        open_source_json = json.load(json_file)

    fake_news_site_list = [fake_news_db_news[i]["siteUrl"]
                           for i in range(len(fake_news_db_news))]
    open_source_site_list = list(open_source_json.keys())

    return fake_news_site_list, open_source_site_list, categories


def get_matching_site(A, B):
    return set(A).intersection(set(B))


def data_dump_fake_news_db(site_list, t1, t2, t3, fake_news_site_list):

    data_list = []

    for site_url, type1, type2, type3 in zip(site_list, t1, t2, t3):
        if site_url not in fake_news_site_list and type(site_url) is not float:

            if str(type2) == 'nan':
                site_category = type1
            elif str(type3) == 'nan':
                site_category = [type1, type2]
            else:
                site_category = [type1, type2, type3]

            site_title, *top_level_domain = str(site_url).split('.')

            if site_url not in fake_news_site_list:
                data_list.append({
                    "siteTitle": site_title,
                    "siteCategory": site_category,
                    "siteUrl": site_url,
                    "siteNotes": ''
                })

    with open(get_data_path('fake_news_sites.json'), 'a') as outfile:
        json.dump(data_list, outfile)


def data_dump_open_source_db(site_list, t1, t2, t3, open_source_site_list):
    data_dict = {}
    for site_url, type1, type2, type3 in zip(site_list, t1, t2, t3):
        if site_url not in open_source_site_list and type(site_url) is not float:
            data_dict[site_url] = {
                "type": type1,
                "2nd type": "" if str(type2) == 'nan' else type2,
                "3rd type": "" if str(type3) == 'nan' else type3,
                "Source Notes (things to know?)": ""
            }

    with open(get_data_path('opensources/sources.json'), 'a') as outfile:
        json.dump(data_dict, outfile)

# fake_news_site_list, open_source_site_list, categories = get_data_json()
# site_list, t1, t2, t3 = get_data_csv()
# data_dump_open_source_db(site_list, t1, t2, t3, open_source_site_list)
