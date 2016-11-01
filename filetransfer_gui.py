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
from tkinter import ttk

import filetransfer_main
import filetransfer_func



def load_gui(self, master):
    
    master.title('Copy Management System')#may need to be moved to _main

    self.style = ttk.Style()
    self.style.configure('TLabel', font = ('Arial', 10))
    self.style.configure('Header.TLabel', font = ('Arial', 20, 'bold'))

    
    # HEADER FRAME
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    
    ttk.Label(self.frame_header, text = "Copy Management System", style = 'Header.TLabel').grid(row = 0, column = 0, pady = (15,0), sticky = W)
    
    # SELECTION FRAME
    self.frame_selection = ttk.Frame(master)
    self.frame_selection.pack()

    
    self.check_time = StringVar()
    filetransfer_func.get_lastcheck(self)
    ttk.Label(self.frame_selection, text = 'Source Folder:').grid(row = 0, column = 0, padx = (10,0), pady = (10,0), sticky = W)
    ttk.Label(self.frame_selection, text = 'Destination Folder:').grid(row = 1, column = 0, padx = (10,0), pady = (10,0), sticky = W)
    ttk.Label(self.frame_selection, text = 'Last Copy Transfer:').grid(row = 5, column = 0, padx = (10,0), sticky = W)
    ttk.Label(self.frame_selection, textvariable = self.check_time).grid(row = 5, column = 1, padx = (10,0), sticky = W)  


    self.src_name = StringVar()
    self.dest_name = StringVar()
    self.entry_source = ttk.Entry(self.frame_selection, width = 50, textvariable = self.src_name)
    self.entry_source.grid(row = 0, column = 1, columnspan = 2, padx = (10,0), pady = (10,0), sticky = E)
    self.entry_destination = ttk.Entry(self.frame_selection, width = 50, textvariable = self.dest_name)
    self.entry_destination.grid(row = 1, column = 1, columnspan = 2, padx = (10,0), pady = (10,0), sticky = E)
    
    ttk.Button(self.frame_selection, text = 'Browse', command = lambda: filetransfer_func.selectsrc(self)).grid(row = 0, column = 3, padx = (10,0), pady = (10,0), sticky = W)
    ttk.Button(self.frame_selection, text = 'Browse', command = lambda: filetransfer_func.selectdest(self)).grid(row = 1, column = 3, padx = (10,0), pady = (10,0), sticky = W)
    ttk.Button(self.frame_selection, text = 'Copy Files', command = lambda: filetransfer_func.copy_path(self)).grid(row = 5, column = 2, pady = (10,10), sticky = W)
    ttk.Button(self.frame_selection, text = 'Clear Fields', command = lambda: filetransfer_func.clear(self)).grid(row = 5, column = 3, padx = (10,0), pady = (10,10))

    
if __name__ == "__main__":
    pass
    
    

