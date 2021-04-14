import json

from news_info import NewsVerdict, AbstractInfo
from url_utils import get_data_path


def append_if_exists(_json, _list, key):
    str_info = _json[key]
    if str_info is not '':
        _list.append(str_info)


class OpenSourcesInfo(AbstractInfo):
    """
    Class containing tags and information about specific domain with fake news based on 
    http://www.opensources.co/ database
    """

    def __init__(self, domain, categories, source_notes, source_desc):
        self.domain = domain
        self.categories = categories
        self.source_notes = source_notes
        self.source_desc = source_desc

    @staticmethod
    def init_categories_descriptions():
        with open(get_data_path('opensources/tags.json')) as data_file:
            return json.load(data_file)

    categories_descriptions = init_categories_descriptions.__func__()

    @staticmethod
    def get_verdict(category):
        return {
            'fake': NewsVerdict.FAKE,
            'satire': NewsVerdict.WARNING,
            'bias': NewsVerdict.FAKE,
            'conspiracy': NewsVerdict.FAKE,
            'rumor': NewsVerdict.WARNING,
            'state': NewsVerdict.WARNING,
            'junksci': NewsVerdict.FAKE,
            'hate': NewsVerdict.WARNING,
            'clickbait': NewsVerdict.WARNING,
            'unreliable': NewsVerdict.WARNING,
            'political': NewsVerdict.WARNING,
            'reliable': NewsVerdict.REAL
        }[category]

    def get_info(self):
        verdicts = [self.get_verdict(x) for x in self.categories]
        categories = self.categories
        descriptions = [self.categories_descriptions[x]
                        for x in self.categories]
        source_notes = [self.domain] + [self.source_desc] + self.source_notes
        return verdicts, categories, descriptions, source_notes

    @staticmethod
    def check(domain, json_sources, source_desc='OpenSource http://www.opensources.co/'):
        json_domain_info = json_sources[domain]

        types_list = []
        append_if_exists(json_domain_info, types_list, 'type')
        append_if_exists(json_domain_info, types_list, '2nd type')
        append_if_exists(json_domain_info, types_list, '3rd type')

        notes_list = []
        append_if_exists(json_domain_info, notes_list,
                         'Source Notes (things to know?)')

        open_source_info = OpenSourcesInfo(domain=domain,
                                           categories=types_list,
                                           source_notes=notes_list,
                                           source_desc=source_desc)
        return open_source_info.get_info()

    @staticmethod
    def can_check_url(domain, json_opensource_data):
        return domain.lower() in json_opensource_data.keys()


class FakeNewsDBInfo(AbstractInfo):
    """
    Class containing tags and information about specific domain with fake news based on the following google sheet:
    https://docs.google.com/spreadsheets/d/1xDDmbr54qzzG8wUrRdxQl_C1dixJSIYqQUaXVZBqsJs/edit#gid=1337422806
    """

    def __init__(self, domain, name, categories, political_alignments, source_notes, source_desc):
        self.domain = domain
        self.name = name
        self.categories = categories
        self.political_alignments = political_alignments
        self.source_notes = source_notes
        self.source_desc = source_desc

    @staticmethod
    def init_categories_descriptions():
        with open(get_data_path('categories.json')) as data_file:
            return json.load(data_file)

    categories_descriptions = init_categories_descriptions.__func__()

    @staticmethod
    def get_verdict(category):
        return {
            'fake news': NewsVerdict.FAKE,
            'satire': NewsVerdict.WARNING,
            'bias': NewsVerdict.FAKE,
            'conspiracy': NewsVerdict.FAKE,
            'rumor': NewsVerdict.WARNING,
            'state': NewsVerdict.WARNING,
            'junk science': NewsVerdict.FAKE,
            'hate': NewsVerdict.WARNING,
            'clickbait': NewsVerdict.WARNING,
            'unreliable': NewsVerdict.WARNING,
            'political': NewsVerdict.WARNING,
            'reliable': NewsVerdict.REAL,
            'celebrity': NewsVerdict.WARNING
        }[category]

    def get_info(self):
        verdicts = [self.get_verdict(x) for x in self.categories]
        categories = self.categories
        descriptions = [self.categories_descriptions[x]
                        for x in self.categories]
        source_notes = [self.domain] + [self.source_desc] + self.source_notes
        if len(self.political_alignments) > 0:
            source_notes.append("Political alignment: " +
                                self.political_alignments[0])
        return verdicts, categories, descriptions, source_notes

    @staticmethod
    def check(domain, json_site, source_desc='FakeNewsDB'):
        name = json_site['siteTitle']

        categories_list = []
        append_if_exists(json_site, categories_list, 'siteCategory')

        political_alignments_list = []
        append_if_exists(json_site, political_alignments_list,
                         'sitePoliticalAlignment')

        source_notes_list = []
        append_if_exists(json_site, source_notes_list, 'siteNotes')

        fakenews_db_info = FakeNewsDBInfo(domain=domain,
                                          name=name,
                                          categories=categories_list,
                                          political_alignments=political_alignments_list,
                                          source_notes=source_notes_list,
                                          source_desc=source_desc)
        return fakenews_db_info.get_info()

    @staticmethod
    def can_check_url(domain, json_data):
        for json_site in json_data:
            if domain.lower() in json_site['siteUrl'].lower():
                return True, json_site
        return False, None
