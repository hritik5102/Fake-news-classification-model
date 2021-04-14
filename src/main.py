import json
import requests

from domain_checker import OpenSourcesInfo, FakeNewsDBInfo
from news_info import AIInfo, AbstractInfo
from url_utils import get_domain, get_data_path


def check_news(url):
    info_list = []

    domain = get_domain(url)

    # Check OpenSource
    json_opensource_data = requests.get(
        'https://raw.githubusercontent.com/BigMcLargeHuge/opensources/master/sources/sources.json').json()
    if OpenSourcesInfo.can_check_url(domain, json_opensource_data):
        (op_info) = OpenSourcesInfo.check(
            domain=domain, json_sources=json_opensource_data)
        info_list.append(op_info)

    # Check Manually added
    with open(get_data_path('manualy_added_sites.json')) as data_file:
        json_manual_data = json.load(data_file)
    if OpenSourcesInfo.can_check_url(domain, json_manual_data):
        (ma_info) = OpenSourcesInfo.check(
            domain=domain, json_sources=json_manual_data)
        info_list.append(ma_info)

    # Check Fakenews
    fakenews_json = requests.get(
        'https://raw.githubusercontent.com/aligajani/fake-news-detector/master/output/fake-news-source.json').json()
    in_fakenews_sources, json_site = FakeNewsDBInfo.can_check_url(
        domain, fakenews_json)
    if in_fakenews_sources:
        (fn_info) = FakeNewsDBInfo.check(domain=domain, json_site=json_site)
        info_list.append(fn_info)

    # Check AI
    can_download_article, article = AIInfo.can_check_url(url, None)
    if can_download_article:
        (ai_info) = AIInfo.check(domain=domain, article=article)
        info_list.append(ai_info)

    return info_list


def info_to_str(info_list):
    info_str = ''
    for info in info_list:
        info_str += AbstractInfo.info_to_str(
            info[0], info[1], info[2], info[3])
    return info_str
