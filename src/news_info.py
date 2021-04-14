from enum import Enum

from newspaper import Article


class AbstractInfo:
    """
    Provides information about the source (site domain or article).
    """

    @staticmethod
    def get_verdict(category):
        """
        Returns verdict based on the given category
        :param category:
        :return: verdict from NewsVerdict enum
        """
        raise NotImplementedError

    @staticmethod
    def check(url, sources):
        """
        Creates AbstractInfo class and checks domain with provided sources

        :param url: url to check
        :param sources: sources with listed domains and their categories
        :return: verdicts, categories, descriptions, source_notes
        """
        raise NotImplementedError

    @staticmethod
    def info_to_str(verdicts, categories, descriptions, source_notes):
        """
        Creates formatted string based on the given information
        :param verdicts: verdict from NewsVerdict enum
        :param categories: categories list
        :param descriptions: descriptions list
        :param source_notes: source notes list
        :return: formatted string based on the given information
        """
        str_result = 'Checking domain: ' + source_notes[0] + '\n'
        str_result += 'Source: ' + source_notes[1] + '\n'
        for i, verdict in enumerate(verdicts):
            str_result += '\tVerdict' + \
                str(i + 1) + ': ' + verdict.value + '\n'
            str_result += '\t\tCategory: ' + categories[i] + '\n'
            str_result += '\t\tDescription: ' + descriptions[i] + '\n'
        for i in range(2, len(source_notes)):
            str_result += '\t\tSource note ' + \
                str(i - 1) + ': ' + source_notes[i] + '\n'
        return str_result

    @staticmethod
    def can_check_url(url, sources):
        raise NotImplementedError


class AIInfo(AbstractInfo):
    @staticmethod
    def can_check_url(article_url, sources):
        # Get newspaper article
        article = Article(article_url)
        article.download()
        if not article.is_downloaded or article.title is None:
            return False, None
        article.parse()
        return True, article

    @staticmethod
    def get_verdict(article):
        if mod.query(article.title) == 1:
            return NewsVerdict.REAL
        else:
            return NewsVerdict.FAKE

    @staticmethod
    def check(domain, article):
        if AIInfo.get_verdict(article) == NewsVerdict.REAL:
            verdicts = [AIInfo.get_verdict(article)]
            categories = ['Real News']
            descriptions = [
                'Analysis performed by artificial intelligence indicate that this article is credible']
        else:
            verdicts = [AIInfo.get_verdict(article)]
            categories = ['Fake News']
            descriptions = [
                'Analysis performed by artificial intelligence indicate that this article is not credible']
        source_notes = [domain] + ['Artificial intelligence'] + \
                       ['WARNING: This result may be inaccurate! This domain wasn\'t categorised on any '
                        'human maintained list thus analysis was performed by machine learning module.']
        return verdicts, categories, descriptions, source_notes


class NewsVerdict(Enum):
    FAKE = 'Fake'
    REAL = 'Real'
    WARNING = 'Warning'
    UNKNOWN = 'Unknown'
