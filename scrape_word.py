import urllib.request
from bs4 import BeautifulSoup as Bs


class ScrapeWord:
    json = {
        'word': '',
        'dic.com': {

        },
        'voc.com': {

        },
    }

    def __init__(self, word):
        self.json['word'] = word

    def scrape(self):
        # Dictionary.com scrape
        soup = Bs(urllib.request.urlopen('https://www.dictionary.com/browse/' + self.json['word']), 'html.parser')
        for num, cls in enumerate(['css-1o58fj8 e1hk9ate4', ]):
            try:
                c1 = soup.find(class_=cls).get_text()
            except AttributeError:
                break
            # self.json['']
        return self.json
