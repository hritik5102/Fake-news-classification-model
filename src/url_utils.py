import os
from urllib.parse import urlparse, ParseResult

import validators

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data_path(path):
    return os.path.join(_ROOT, 'json_local', path)


def format_url(url):
    """    
    Formats url by adding 'http://' if necessary and deleting 'www.' 

    :param url: ulr to article or domain
    :return: formatted url e.g. the following urls: 
                'http://www.google.pl/', 'google.pl/', 'google.pl/', 'www.google.pl/', 
                'http://google.pl/', 'https://www.google.pl/'
              will be all formatted to: http://google.pl/
    """
    parsed_url = urlparse(url, 'http')
    netloc = parsed_url.netloc or parsed_url.path
    path = parsed_url.path if parsed_url.netloc else ''
    netloc = netloc.replace('www.', '')

    parsed_url = ParseResult('http', netloc, path, *parsed_url[3:])
    if not validators.url(parsed_url.geturl()):
        raise ValueError('Provided url=' + url + ' is not valid')
    return parsed_url.geturl()


def get_domain(url):
    """
    Extracts domain from url
    :param url: ulr to article or domain
    :return: domain e.g. google.pl
    """
    return urlparse(format_url(url)).hostname


# print(get_domain('https://www.washingtonpost.com/politics/2021/04/01/matt-gaetzs-claim-that-travel-records-debunk-allegations-against-him/'))
