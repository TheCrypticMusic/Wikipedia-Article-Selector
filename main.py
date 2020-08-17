import requests
from bs4 import BeautifulSoup
import re 


class ArticleSelector:
    

    url = 'https://en.wikipedia.org/wiki/'
    infomation = {}
    search_not_found = 'https://en.wikipedia.org/w/index.php?sort=relevance&search='
    search_names = {}
    section_text = []

    def __init__(self, search_term):
        self.search_term = search_term
        
    def test_connection(self):
        self.res = requests.get(f'{self.url}{self.search_term}')
        if self.res.status_code == 200:
            print('Article found')
            self.__web_scraper()
        else:
            print('Article not found. Did you mean:')
            self.__article_not_found()
            self.__choose_new_article()
            
            
    def __article_not_found(self):
        
        self.res = requests.get(f'{self.search_not_found}{self.search_term}')
        self.search_soup = BeautifulSoup(self.res.text, 'lxml')
        self.search_results = self.search_soup.find('ul', {'class': 'mw-search-results'}).find_all_next('div', {'class': 'mw-search-result-heading'})
        # Enumerate to add numbers to list
        
        for number, search in enumerate(self.search_results):
            search = search.get_text()
            self.search_names.setdefault(number, search)
        
        for key, values in self.search_names.items():
            print(key, values)
    
    def __choose_new_article(self):
        self.choose_article = int(input())
        # Need to remove search headings with brackets
        self.new_search = self.search_names.get(self.choose_article)
        self.res = requests.get(f'{self.url}{self.new_search}')
        self.__web_scraper()
            
    def __web_scraper(self):
        self.soup = BeautifulSoup(self.res.text, 'lxml')
        self.navigation = self.soup.find('div', {'role': 'navigation'}).get_text().split('\n')
        # Regular expression used to find every section of the page in the navigation box.
        self.r = re.compile(r"([0-9]+)")
        
        self.page_links = list(filter(self.r.match, self.navigation))
        # Puts the contents into the a dict - key = num, value = section name
        # The number will be used to call the section and display it to the user
        for i in self.page_links:
            self.index = i.split(' ', 1)
            self.infomation.setdefault(self.index[0], self.index[1])
        
        # Displays to the user all the sections on that particular Wikipedia page\
        #for number, section_name in self.infomation.items():
            #print(number, section_name)
        
    def display_content(self, section):
        self.section = section
        #self.number = number   
        #self.user_input = input('Enter a number: ')
        #self.page_section = self.infomation.get('1').split(" ")
        # Wikipedia uses the section name as ID tag with underscores for spaces EG: Toxicity of seeds = Toxicity_of_seeds
        #self.id_search = "_".join(self.page_section)


        self.sub_category = self.soup.find('div', {'class': 'mw-parser-output'}).find('span', {'id': f'{self.section}'})
        for i in self.sub_category.find_all_next(['p', 'h2', 'h3', 'h4', 'li']):
            if i.name == 'p' or i.name == 'h3' or i.name == 'h4' or i.name == 'li':
                self.section_text.append(i.get_text())
            else:
                break
            
            # else:
            #     print('Would you like to view another section?')
            #     self.choice = input('Yes or no? (Enter: Yes/ No): ')
            #     if self.choice.lower() == 'yes':
            #         self.__web_scraper()
            #     else:
            #         print('Okay. Shutting down...')
            #         break



