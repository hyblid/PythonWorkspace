"""
The application/controller class for Movie Data Entry
"""

import tkinter as tk
from tkinter import ttk
from . import views as v
from . import models as m
import sqlite3

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = m.Movie("Terminator", "1999","5")
        self.title("Movie Data Entry Application")
        self.columnconfigure(0, weight=1)
        self.geometry("650x300")

        ttk.Label(self, text="Movie Data Entry Application", font=("TkDefaultFont", 16)).grid(row=0)

        self.recordform = v.DataRecordForm(self, self.model)
        self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))
        #  in views.py ---> self.event_generate('<<SaveRecord>>')
        self.recordform.bind('<<DeleteRecord>>', self._on_delete)
        self.recordform.bind('<<ResetRecord>>', self._on_reset)
        self.recordform.bind('<<<ModifyRecord>>', self._on_modify)
        self.recordform.bind('<<SaveRecord>>', self._on_save)
        self.recordform.bind('<<ViewRecord>>', self._on_view)
        
        # status bars
        # self.status = tk.StringVar()
        # self.statusbar = ttk.Label(self, textvariable=self.status)
        # self.statusbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)

        # self._records_saved = 0
        
    def _on_save():
        #with sqlite3.connect("compayny,db") as db:
            # cursor = db.cursor()
            # cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEES (
            #       id integer PRIMARY KEY AUTO_INCREMENT,
            #       name text NOT NULL,
            #       dept text NOT NULL,
            #       salary integer);""")
    
            # cursor.execute("""INSERT INTO employees (id,name,dept,salary) 
            #       VALUES("1", "bob", "Sales", "25000")""")
            # db.commit()
        pass     
    def _on_view():
        pass    
    def _on_modify():
        pass    
    def _on_reset():
        pass    
    def _on_delete():
        pass    
    