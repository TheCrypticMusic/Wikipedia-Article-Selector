import requests
from bs4 import BeautifulSoup
import re 


class ArticleSelector:
    
    url = f'https://en.wikipedia.org/wiki/'
    infomation = {}

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
            self.infomation.setdefault(i)
        
        
        # Separate sections of the page 

        self.article = self.soup.find('div', {'class': 'mw-parser-output'})
        for i in self.article:
            self.sub_cats = self.soup.find('span', {'id': 'Common_elements'})
            if i.name == 'p':
                print(i.text)
            if i.name == 'h2':
                break
            
        # for child in self.section.next_sibling:
        #     print(child)


        # for elem in self.section.find_all_next('p'):
        #     print(elem)
       
        



        #self.titles = self.soup.find('p')
        # for elem in self.titles.next_siblings:
        #     if elem.name != 'h2':
        #         continue
        #     print(elem)


        # TODO: PUT CONTENT INTO A DICT
        # T0DO: CREATE GUI
       


user_article = ArticleSelector('football')
user_article.test_connection()
user_article.web_scraper()
