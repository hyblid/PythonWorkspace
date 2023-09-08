"""
The application/controller class for Movie Data Entry
"""

import tkinter as tk
from tkinter import ttk
from . import views as v
from . import models as m


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = m.Movie("Terminator", "1999","5")
        self.title("Movie Data Entry Application")
        self.columnconfigure(0, weight=1)

        ttk.Label(self, text="Movie Data Entry Application", font=("TkDefaultFont", 16)).grid(row=0)

        self.recordform = v.DataRecordForm(self, self.model)
        self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))
        #  in views.py ---> self.event_generate('<<SaveRecord>>')
        # self.recordform.bind('<<SaveRecord>>', self._on_save)
        
        # status bars
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)

        self._records_saved = 0