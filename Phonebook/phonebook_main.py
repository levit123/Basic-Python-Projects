from tkinter import *
import tkinter as tk
from tkinter import messagebox

#imports the code from the other Python files related to this project
import phonebook_gui
import phonebook_func

#defines a class that inherits from the "Frame" tkinter class
class ParentWindow(Frame):
    #constructor for the "ParentWindow" class, which calls the constructor for the "Frame" tkinter class
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #defines the configuration for the frame
        self.master = master
        self.master.minsize(500, 300) #minimum height and width
        self.master.maxsize(500, 300) #maximum height and width

        #calls the "center_window" method from "phonebook_func.py", which centers the program on the user's screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook App")
        self.master.configure(bg="#F0F0F0")

        #calls the "protocol" method, which is a tkinter method that handles if the user clicks the "X" to close the program
        #(also uses the "ask_quit" method from "phonebook_func.py"
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #calls the "load_gui" function from "phonebook_gui" to create and load the GUI widgets
        phonebook_gui.load_gui(self)

        #instantiates an object of the tkinter menu dropdown, which appears at the top of the window
        menuBar = Menu(self.master)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q", command=lambda: phonebook_func.ask_quit(self))
        menuBar.add_cascade(label="File", underline=0, menu=fileMenu)

        #defines a specific dropdown column
        #NOTE: tearoff=0 means that it will not seperate from menuBar
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_separator()
        helpMenu.add_command(label="How to use this program")
        helpMenu.add_separator()
        helpMenu.add_command(label="About This Phonebook App")
        menuBar.add_cascade(label="Help", menu=helpMenu)

        #applies the "config" method of the widget to display the menu
        self.master.config(menu=menuBar, borderwidth='1')

#the initial part of the program that runs, which begins the chain of events to create and load the GUI and it's functionality
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()