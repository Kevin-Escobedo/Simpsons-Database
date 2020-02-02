#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import simpsons_database
import tkinter
import sys
import os

class DatabaseUI:
    def __init__(self):
        '''Constructor for Database GUI'''
        self.root_window = tkinter.Tk()
        self.root_window.geometry("300x125")
        self.root_window.iconbitmap(self.resource_path("simpsons.ico"))
        self.root_window.resizable(0, 0)
        self.root_window.title("Simpsons Database")
        self.label = tkinter.Label(self.root_window, text = "Simpsons Database")
        self.entry = tkinter.Entry(self.root_window, width = 45)
        self.search_button = tkinter.Button(self.root_window, text = "Search", command = self.search)
        self.database = simpsons_database.SimpsonsDatabase()
        self.variable = tkinter.StringVar()
        self.show = tkinter.Label(self.root_window, textvariable = self.variable)
        self.variable.set("")

    def resource_path(self, relative_path:str):
        '''Get absolute path to resource, works for dev and for PyInstaller'''
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def search(self) -> None:
        '''Gets the entry and returns information from the database'''
        query = self.entry.get()
        if len(query) != 0:
            try:
                query = int(query)
                response = self.database.get_episode_title(query)
            except ValueError:
                response = self.database.get_episode_number(query)
            self.variable.set(response)

    def key(self, event):
        '''Handles keyboard input'''
        if event.keysym == "Return":
            self.search()

    def run(self):
        '''Runs the GUI'''
        self.label.grid(row = 0, column = 1, columnspan = 3)
        self.entry.grid(row = 1, column = 1, columnspan = 3)
        self.search_button.grid(row = 2, column = 1, columnspan = 3)
        self.show.grid(row = 3, column = 1, columnspan = 3)

        self.root_window.bind("<KeyPress>", self.key)
        self.root_window.mainloop()


if __name__ == "__main__":
    DatabaseUI().run()



