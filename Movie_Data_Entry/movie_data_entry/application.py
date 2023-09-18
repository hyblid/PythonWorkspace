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
        self.geometry("650x350")
        self.config(padx=5, pady=5)
        self.resizable(True, True)
        self.iconbitmap("tool_box.ico")
        
        # style = ttk.Style()
        # style.theme_use('clam')

        ttk.Label(self, text="Movie Data Entry Application", 
                  font=("TkDefaultFont", 16)).grid(row=0)

        self.recordform = v.DataRecordForm(self, self.model)
        self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))
        self.recordform.bind('<<DeleteRecord>>', self._on_delete)
        self.recordform.bind('<<ResetRecord>>', self._on_reset)
        self.recordform.bind('<<ModifyRecord>>', self._on_modify)
        self.recordform.bind('<<SaveRecord>>', self._on_save)
        self.recordform.bind('<<ViewRecord>>', self._on_view)
        
    def connect_db(self):
        with sqlite3.connect(self.DB_NAME) as db:
            cursor = db.cursor()
    
            cursor.execute("""CREATE TABLE IF NOT EXISTS MOVIES (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title text NOT NULL,
                 year text NOT NULL,
                 stars text NOT NULL);""")
        return db, cursor
    
    def _on_save(self, *_):
        #creat or add record
        db, cursor = self.connect_db()
  
        title = self.recordform.txt_title.get()
        year = self.recordform.txt_year.get()
        stars = self.recordform.txt_stars.get()
              
        cursor.execute("""INSERT INTO movies (title, year, stars) VALUES(?,?,?)""", 
                    (title, year, stars))
        db.commit()
            
            # self.recordform.reset_entry() 
        self._on_reset()
        cursor.execute("SELECT * FROM MOVIES")
        print("Record was saved", cursor.fetchall())  

    def _on_view(self, *_):
        #clear before clicked view
        self._on_reset()
        
        with sqlite3.connect(self.DB_NAME) as db:
            cursor = db.cursor()
     # Delete for refresh tree not duplicate s
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
            print("Treeview was displayed!",cursor.fetchall())
            self.recordform.status_label.config(text="Treeview was displayed!")
            self.recordform.tree.bind("<Double-1>", self.OnDoubleClick)
            
    def OnDoubleClick(self, event):
        current_item = self.recordform.tree.item(self.recordform.tree.focus())
        detail_item = list(current_item.get("values"))
        print("You clicked printed title:{0} year:{1} stars:{2}"
            .format(detail_item[1], detail_item[2], detail_item[3]))
        # insert values to Entries
        self.recordform.txt_title.insert(tk.END, detail_item[1])
        self.recordform.txt_year.insert(tk.END, detail_item[2])
        self.recordform.txt_stars.insert(tk.END, detail_item[3])
        # fix title is disable for modifying record
        self.recordform.txt_title.config(state="disabled")        
         
    def _on_modify(self, *_):
        title = self.recordform.txt_title.get()
        year = self.recordform.txt_year.get()
        stars =  self.recordform.txt_stars.get()        
        db, cursor = self.connect_db()
        cursor.execute("""UPDATE movies SET year=?, stars=? WHERE title=?"""
                       , (year, stars, title)) 
        db.commit()
        print(f"year:{year} and stars:{stars} was update for title:{title}")    
         
    def _on_reset(self, *_):
        self.recordform.tree.delete(*self.recordform.tree.get_children())
        self.recordform.txt_title.delete(0, tk.END)  
        self.recordform.txt_year.delete(0, tk.END)  
        self.recordform.txt_stars.delete(0, tk.END)  
        self.recordform.update()   
        
    def _on_delete(self, *_):
        title = self.recordform.txt_title.get() 
        if not title:
            db, cursor = self.connect_db()   
            cursor.execute("""DELETE FROM movies WHERE title=?""", (title,)) 
            # cursor.execute("""DELETE FROM movies WHERE title='Xman'""") 
            db.commit()
            print(f"title:{title} was deleted!")
            self._on_view()  
    