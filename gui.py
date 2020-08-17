import tkinter as tk
from main import ArticleSelector


class App(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.widgets()
        self.pack()
        
        
    def widgets(self):
        """Creates the widgets for the GUI"""
        self.title = tk.Label(self, text='Wikipedia Article Selector', font='Aerial 22 bold')
        self.title.pack()

        self.description = tk.Label(self, text='Please enter a topic to search')
        self.description.pack(pady=10)

        self.search_bar = tk.Entry(self)
        self.search_bar.bind('<Return>', self.user_search)
        self.search_bar.pack()
        
        # ADD FUNCTION
        self.search_bar.pack(ipadx=70, pady=10)


        self.display_navigation_results = tk.Text(self, width=20, height=30)
        
        self.display_navigation_results.pack(side=tk.LEFT, padx=10, pady=10)    
        
        self.display_content_results = tk.Text(self, width=50, height=30)
        
        self.display_content_results.pack(side=tk.LEFT, padx=10, pady=10)
        
        

    def user_search(self, event=None):
        self.search = self.search_bar.get()
        self.search_bar.delete(0, 'end')
        self.test = ArticleSelector('Apple')
        self.test.test_connection()
        self.navigation_content()
        #self.search = self.search_bar.get()
        self.results_contents() 
    
    def navigation_content(self, event=None):
        for number, section in reversed(self.test.infomation.items()):
            self.display_navigation_results.insert('1.0', f'\n{number} {section}')
        
    def results_contents(self, event=None):
        self.page_section = self.test.infomation.get('3').split(" ")
        self.id_search = "_".join(self.page_section)
        self.test.display_content(self.id_search)
        #self.content = self.test.infomation.get('5')
        self.display_content_results.insert('1.0', f'{self.test.section_text}')

        
        #for number, section in self.test.infomation.items():
            #self.display_navigation_results.insert('1.0', f'\n{number} {section}')

root = tk.Tk()

app = App(master=root)
root.mainloop()
