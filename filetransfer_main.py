# Python:  3.5.2
#
# Author:  Michael Harrison
#
# Version: 1.1
#
# Purpose: The purpose of this drill is to create a UI for a file copying
# module which allows the user to browse and select a folder containing
# files to be copied which have been added or modified in the past 24 hours to
# to another folder of the user's selection.


from tkinter import *
import tkinter as ttk

import filetransfer_gui
import filetransfer_func

filetransfer_func.create_db()

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        #Master frame configuration
        self.master = master
        self.master.minsize(580,170)
        self.master.maxsize(580,170)
        
        filetransfer_func.center_window(self, 500, 300)
        self.master.title("File Transfer Program")
        #self.master.configure(background = somecolor)
        self.master.protocol("WM_DELETE_WINDOW", lambda: filetransfer_func.ask_quit(self))
        arg = self.master
        
        #load widgets
        filetransfer_gui.load_gui(self, master)
        
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", underline=1, command = lambda: filetransfer_func.ask_quit(self)) #currently no functionality
        menubar.add_cascade(label="File", menu = filemenu)
        self.master.config(menu=menubar, borderwidth='1')                             

def main():
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
if __name__ == "__main__": main()
