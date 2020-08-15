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
        self.description.pack()

        self.search_bar = tk.Entry(self)
        self.search_bar.bind('<Return>') # ADD FUNCTION
        self.search_bar.pack(padx=20, pady=15)


        self.display_text = tk.Text(self, width=40, height=30)
        self.display_text.pack()

root = tk.Tk()
root.geometry('300x300')
app = App(master=root)
root.mainloop()