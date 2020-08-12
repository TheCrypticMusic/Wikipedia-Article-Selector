import requests
from bs4 import BeautifulSoup


class ArticleSelector:
    
    url = f'https://en.wikipedia.org/wiki/'


    def __init__(self, search_term):
        self.search_term = search_term
        
        
    def test_connection(self):
        self.res = requests.get(f'{self.url}{self.search_term}')
        if self.res.status_code == 200:
            print('Good Link')
        else:
            print('Bad Link')

    def web_scraper(self):
        self.soup = BeautifulSoup(self.res.text, 'lxml')
        self.title = self.soup.find('h1', {'class': 'firstHeading'}).get_text()
        
        
       


user_article = ArticleSelector('football')
user_article.test_connection()
user_article.web_scraper()
user_article
