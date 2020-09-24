from main import ArticleSelector
import tkinter as tk


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
        
        self.search_bar.pack(ipadx=70, pady=10)
        self.display_navigation_results = tk.Text(self, width=20, height=30)
        self.display_navigation_results.pack(side=tk.LEFT, padx=10, pady=10)    
        self.display_content_results = tk.Text(self, width=50, height=30)
        self.display_content_results.pack(side=tk.LEFT, padx=10, pady=10)
        
    def user_search(self, event=None):
        self.search = self.search_bar.get()
        self.user = ArticleSelector(self.search)
        
        
        
        
        self.search_bar.delete(0, 'end')
        self.display_content_results.insert('1.0', '')
        
        for i, j in reversed(self.user.infomation.items()):
           
            self.display_navigation_results.insert('1.0', f"{i} {j}\n")



root = tk.Tk() 
app = App(master=root)
root.mainloop()
