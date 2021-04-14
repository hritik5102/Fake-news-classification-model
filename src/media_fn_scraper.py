import io
import requests
import bs4
from bs4 import BeautifulSoup
from url_utils import get_data_path


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


# output_file = open('output.txt', "r")
# content = output_file.read()
# # print(content)

# content_list = content.split('\n')
# # print(content_list)
# site_title, site_link, site_categories = [], [], []
# for i in content_list:
#     x = i.split(', ')
#     if len(x) != 0:
#         try:
#             site_title.append(x[0])
#             site_link.append(x[1])
#             # site_categories.append(x[2])
#         except Exception as ec:
#             print(i)

# # # print("2nd Amendment Daily News (secondamendmentdaily.com)".split('('))
# print(site_title[:5], site_link[:5], site_categories[:5])

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
    # print(output_list[:5])
    for i in output_list[344:]:
        get_categories(i)


# get_fn_categories()

A = {'rightwingnews.com', 'lewrockwell.com', 'vdare.com', 'clashdaily.com', 'usasupreme.com', 'uschronicle.com', 'other98.com', 'lifesitenews.com', 'thefederalistpapers.org', 'dcclothesline.com', 'newswithviews.com', 'oathkeepers.org', 'anonews.co', 'libertytalk.fm', 'projectveritas.com', 'thegatewaypundit.com', 'beforeitsnews.com', 'dailyheadlines.net', 'breaking911.com', 'pjmedia.com', 'cap-news.com', 'allnewspipeline.com', 'therightstuff.biz', '100percentfedup.com', 'amren.com', 'redstate.com', 'libertynews.com', 'conservativepapers.com', 'thepoliticalinsider.com', 'heartland.org', 'now8news.com', 'ilovemyfreedom.org', 'wnd.com', 'canadafreepress.com', 'teaparty.org', 'sputniknews.com', 'yesimright.com', 'redstatewatcher.com', 'americanpatriotdaily.com', 'truthandaction.org', 'occupydemocrats.com', 'prntly.com', 'americanthinker.com', 'bipartisanreport.com', 'ruptly.tv', 'unclesamsmisguidedchildren.com', 'judicialwatch.org', 'americanlookout.com', 'conservapedia.com', 'conservativefiringline.com', 'lifenews.com', 'presstv.com',
     'pravdareport.com', 'notallowedto.com', 'blackgenocide.org', 'madworldnews.com', 'thefreepatriot.org', 'theblaze.com', 'breitbart.com', 'angrypatriotmovement.com', 'frontpagemag.com', 'dailybuzzlive.com', 'unz.com', 'thebostontribune.com', 'barenakedislam.com', 'theduran.com', 'pamelageller.com', 'russia-insider.com', 'conservativedailypost.com', 'nationalvanguard.org', 'awm.com', 'centerforsecuritypolicy.org', 'conservativebyte.com', 'hangthebankers.com', 'americasfreedomfighters.com'}

B = {'rightwingnews.com', 'theblacksphere.net', 'clashdaily.com', 'home.nra.org', 'pmnightlynews.com', 'other98.com', 'eaglerising.com', 'vidmax.com', 'bb4sp.com', 'libertytalk.fm', 'beforeitsnews.com', 'dailyheadlines.net', 'pjmedia.com', 'projectveritas.com', 'leftaction.com', 'cap-news.com', 'libertynews.com', 'now8news.com', 'personalliberty.com', 'front.moveon.org', 'ilovemyfreedom.org',
     'canadafreepress.com', 'redstatewatcher.com', 'occupydemocrats.com', 'conservativepost.com', 'townhall.com', 'bipartisanreport.com', 'unclesamsmisguidedchildren.com', 'americanlookout.com', 'thedcgazette.com', 'blackgenocide.org', 'dailybuzzlive.com', 'nowthisnews.com', 'thefederalist.com', 'thebostontribune.com', 'truthinmedia.com', 'conservativedailypost.com', 'prntly.com'}

print(A.intersection(B))


# Conspiracy -> conspiracy
# Imposter Site -> Imposter site
# False -> False information
# Fake News -> Fake news
# Conspiracies -> conspiracy
