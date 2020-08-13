import requests
from bs4 import BeautifulSoup
import re 


class ArticleSelector:
    
    url = 'https://en.wikipedia.org/wiki/'
    infomation = {'0': 'Intro'}
    
   
    
   
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
        
        self.navigation = self.soup.find('div', {'role': 'navigation'}).get_text().split('\n')
        self.r = re.compile(r"([0-9]+)")
        
        self.page_links = list(filter(self.r.match, self.navigation))
        
        # Puts the contents into the a dict - need to pack values into dict next
        for i in self.page_links:
            self.index = i.split(' ', 1)
            self.infomation.setdefault(self.index[0], self.index[1])
        
        print(self.infomation)
        # Separate sections of the page 
        for i, j in self.infomation.items():
            print(i, j)
        
        # TEST: CHANGE TO INPUT ONCE COMPLETED
        
        self.user_input = input('Enter a number: ')
        self.f = self.infomation.get(self.user_input).split(" ")
        
        self.id_search = "_".join(self.f)
        
        
        self.sub_cats = self.soup.find('div', {'class': 'mw-parser-output'}).find('span', {'id': f'{self.id_search}'})
       
        
        for i in self.sub_cats.find_all_next(['p', 'h2', 'h3', 'h4']):
            if i.name == 'p' or i.name == 'h3' or i.name == 'h4' or i.name == 'li':
                 print(i.text)
            else:
                 break
        
    



user_article = ArticleSelector('apple')
user_article.test_connection()
user_article.web_scraper()
