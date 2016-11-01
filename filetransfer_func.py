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

import os
from tkinter import *
import shutil
import time
import sqlite3
from datetime import datetime

import filetransfer_main
import filetransfer_gui

#=====================================================================================================================================
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (w/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Okay to exit application?"):
        #this closes app; os.exit(0) is method to ensure that program releases all memory after program is quit, giving user back full memory
        self.master.destroy()
        os._exit(0)
        
#======================================================================================================================================================


# creates database to store timestamp of last file transfer
def create_db():
    conn = sqlite3.connect('db_filecheck.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_lastfilecheck(\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_lastcheck TEXT \
                    );")
        conn.commit()
    conn.close()


def selectsrc(self):
    src_name = filedialog.askdirectory()
    self.src_name.set(src_name) 


def selectdest(self):
    dest_name = filedialog.askdirectory()
    self.dest_name.set(dest_name)


    
def copy_path(self):
    src = self.src_name.get()
    dest = self.dest_name.get()
    if moveFiles(src, dest):
        check_time = datetime.now()
        
        print(check_time)
        self.check_time.set(check_time)
        add_filecheck(self)
        successAlert(self, dest)
        clear(self)
    else:
        failureAlert(self)
    
          
def moveFiles(src,dest):
    day = 24 * 60 * 60 #unix time of 24 hours
    try:
        for filename in os.listdir(src):
            modFile = os.path.getmtime(src + '/{}'.format(filename))
            modPeriod = time.time() - modFile
            if filename.endswith(".txt") and modPeriod <= day:
                shutil.copy2(src + '/{}'.format(filename), dest)
        return True
    except:
        return False

#Inserts last file transfer timestamp as label in GUI    
def add_filecheck(self):
    varFileCheck = self.check_time.get()
    conn = sqlite3.connect('db_filecheck.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO tbl_lastfilecheck(col_lastcheck) VALUES (?)""", (varFileCheck,))
        conn.commit()
    conn.close()


#accesses db for last file transfer timestamp
def get_lastcheck(self):
    conn = sqlite3.connect('db_filecheck.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_lastcheck FROM tbl_lastfilecheck ORDER BY ID DESC LIMIT 1""")
        varCheck = cur.fetchone()
        self.check_time.set(varCheck) 
        

    

def successAlert(self, dest):
    messagebox.showinfo(title = "File Copy Status", message = 'Files successfully copied to: \n\n' + dest)


def failureAlert(self):
    messagebox.showerror(title = "File Copy Status", message = 'Files failed to copy')
    

def clear(self):
    self.entry_source.delete(0, 'end')
    self.entry_destination.delete(0, 'end')


if __name__ == "__main__":
    pass
