import urllib.request
from bs4 import BeautifulSoup as Bs


class ScrapeWord:
    json = {
        # This is the state for whether the program grabbed the word
        'state': False,
        'word': '',
        'dic.com': {
            'state': False,
            '': ''
        },
        'voc.com': {
            'state': False,
            'long': '',
            'short': '',
            'definition': ''
        },
        # 'cam.com': {
        #
        # },
    }

    def __init__(self, word):
        self.json['word'] = word

    def scrape(self):
        # Dictionary.com scrape
        soup = Bs(urllib.request.urlopen('https://www.dictionary.com/browse/' + self.json['word']), 'html.parser')
        for cls in ['css-1o58fj8 e1hk9ate4', ]:
            try:
                c1 = soup.find(class_=cls).get_text()
            except AttributeError:
                break
            # self.json['']
        # Vocabulary.com scrape
        soup = Bs(urllib.request.urlopen('https://www.vocabulary.com/dictionary/' + self.json['word']), 'html.parser')
        for cls in ['long', 'short', 'definitions']:
            try:
                c1 = soup.find(class_=cls).get_text()
            except AttributeError:
                break
            # self.json['']

        # # Cambridge.com support is currently under development since its classes are much messier...
        # # Cambridge.com scrape
        # soup = Bs(urllib.request.urlopen('https://dictionary.cambridge.org/dictionary/english/' + self.json['word']),
        #           'html.parser')
        # for cls in ['css-1o58fj8 e1hk9ate4', ]:
        #     try:
        #         c1 = soup.find(class_=cls).get_text()
        #     except AttributeError:
        #         break
        #     # self.json['']

        return self.json
