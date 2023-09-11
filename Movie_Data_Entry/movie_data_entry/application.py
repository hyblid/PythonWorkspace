"""
The application/controller class for Movie Data Entry
"""

import tkinter as tk
from tkinter import ttk
from . import views as v
from . import models as m
import sqlite3


PINK = "#FFE4C0"
PINK = "#FFBBBB"
BLUE = "#BFFFF0"
GREEN = "#BFFFF0"

class Application(tk.Tk):
    
    DB_NAME = "movie.db"
    
    def __init__(self, *args, **kwargs):
        self.PINK = "#FFBBBB"
        super().__init__(*args, **kwargs)

        self.model = m.Movie()
        self.title("Movie Data Entry Application")
        self.columnconfigure(0, weight=1)
        self.geometry("650x300")
        self.config(padx=5, pady=5, bg=PINK)
        self.resizable(True, True)
        
        # style = ttk.Style()
        # style.theme_use('clam')

        ttk.Label(self, text="Movie Data Entry Application", font=("TkDefaultFont", 16), background=PINK).grid(row=0)

        self.recordform = v.DataRecordForm(self, self.model)
        self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))
        #  in views.py ---> self.event_generate('<<SaveRecord>>')
        self.recordform.bind('<<DeleteRecord>>', self._on_delete)
        self.recordform.bind('<<ResetRecord>>', self._on_reset)
        self.recordform.bind('<<ModifyRecord>>', self._on_modify)
        self.recordform.bind('<<SaveRecord>>', self._on_save)
        self.recordform.bind('<<ViewRecord>>', self._on_view)
        
        # status bars
        # self.status = tk.StringVar()
        # self.statusbar = ttk.Label(self, textvariable=self.status)
        # self.statusbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)

        # self._records_saved = 0
        
    def connect_db(self):
        with sqlite3.connect(self.DB_NAME) as db:
            cursor = db.cursor()
    
            cursor.execute("""CREATE TABLE IF NOT EXISTS MOVIES (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title text NOT NULL,
                 year text NOT NULL,
                 stars text NOT NULL);""")
        return db
    
    def _on_save(self, *_):
        #creat record file
        with sqlite3.connect(self.DB_NAME) as db:
            cursor = db.cursor()
    
            cursor.execute("""CREATE TABLE IF NOT EXISTS MOVIES (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title text NOT NULL,
                 year text NOT NULL,
                 stars text NOT NULL);""")
  
            title = self.recordform.txt_title.get()
            year = self.recordform.txt_year.get()
            stars = self.recordform.txt_stars.get()
                
            cursor.execute("""INSERT INTO movies (title, year, stars) VALUES(?,?,?)""", 
                    (title, year, stars))
            db.commit()
            
            self.recordform.reset_entry() 
            cursor.execute("SELECT * FROM MOVIES")
            print("Record was saved", cursor.fetchall())  

    def _on_view(self, *_):
        with sqlite3.connect(self.DB_NAME) as db:
            cursor = db.cursor()
     # Delete for refresh tree not duplicate s
        # refresh_tree()
            self.recordform.tree.column("# 1", anchor=tk.CENTER, stretch=tk.NO, width=50)
            self.recordform.tree.heading("# 1", text="id")
            self.recordform.tree.column("# 2", anchor=tk.CENTER, stretch=tk.NO, width=150)
            self.recordform.tree.heading("# 2", text="Title")
            self.recordform.tree.column("# 3", anchor=tk.CENTER, stretch=tk.NO, width=150)
            self.recordform.tree.heading("# 3", text="Year")
            self.recordform.tree.column("# 4", anchor=tk.CENTER, stretch=tk.NO, width=150)
            self.recordform.tree.heading("# 4", text="Stars")

            # Insert the data in Treeview widget
            cursor.execute("SELECT * FROM MOVIES")
            for movie in cursor.fetchall():
                    self.recordform.tree.insert('', 'end', text="item",
                            values=(movie[0], movie[1], movie[2], movie[3]))
        
            # self.tree.bind("<Double-1>", OnDoubleClick)
            print("Treeview was displayed!",cursor.fetchall())
            
        
    def _on_modify(self, *_):
        pass    
    def _on_reset(self, *_):
        pass    
    def _on_delete(self, *_):
        pass    
    