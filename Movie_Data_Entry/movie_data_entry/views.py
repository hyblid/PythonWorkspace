import tkinter as tk
from tkinter import ttk

class DataRecordForm(tk.Frame):
  """The input form for our widgets"""
 
  def __init__(self, parent, model, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    self.model= model
    fields = self.model.fields

    # Build the form
    self.columnconfigure(0, weight=1)

    # Record info section
    self.treeview_frame = ttk.LabelFrame(self, text="Movie Record", height= 200)
    self.treeview_frame.grid()

    self.tree = ttk.Treeview(self.treeview_frame, columns=("id", "Title", "Year", "Stars"),
                             selectmode='browse',show='headings', height=5)

    self.tree.grid(sticky=tk.W + tk.E, ipadx= 1, ipady=1, column=1, row=0)
  
    self.scrollbar = ttk.Scrollbar(self.treeview_frame, orient=tk.VERTICAL, command=self.tree.yview)
    self.scrollbar.grid(sticky=tk.N + tk.S + tk.W, column=0, row=0)

    #entries
    self.entry_frame = ttk.LabelFrame(self, text="Movie Detail")
    self.entry_frame.grid(sticky=tk.W + tk.E)
    
    frame_content_title = ttk.Label(self.entry_frame, text="Title").grid(column=0, row=0, sticky=tk.E +tk. W)
    self.txt_title = ttk.Entry(self.entry_frame, width=32)
    self.txt_title.grid(column=0, row=1, sticky=(tk.E + tk.W), padx= 4, pady=4)
    self.frame_content_year = ttk.Label(self.entry_frame, text="Year").grid(column=1, row=0, sticky=tk.E + tk.W)
    self.txt_year = ttk.Entry(self.entry_frame, width=32)
    self.txt_year.grid(column=1, row=1, sticky=(tk.E + tk.W), padx= 4, pady=4)
    self.frame_content_stars = ttk.Label(self.entry_frame, text="Stars").grid(column=2, row=0, sticky=tk.E + tk.W)
    self. txt_stars = ttk.Entry(self.entry_frame, width=32)
    self.txt_stars.grid(column=2, row=1, sticky=(tk.E + tk.W), padx= 4, pady=4)

    #buttons
    self.buttons = ttk.LabelFrame(self, text="Operations")
    self.buttons.grid(sticky=tk.W + tk.E)
    self.exitbutton =ttk.Button(self.buttons, text="Exit", width= 15, command=self.quit)
    self.exitbutton.pack(side=tk.RIGHT, padx=3, pady=2)
    self.deletebutton = ttk.Button(self.buttons, text="Delete", width= 15, command=self._on_delete)
    self.deletebutton.pack(side=tk.RIGHT, padx=3, pady=2)
    self.resetbutton = ttk.Button(self.buttons, text="Reset", width= 15, command=self._on_reset)
    self.resetbutton.pack(side=tk.RIGHT, padx=3, pady=2)
    self.modifybutton = ttk.Button(self.buttons, text="Modify", width= 15, command=self._on_modify)
    self.modifybutton.pack(side=tk.RIGHT, padx=3, pady=2)
    self.savebutton = ttk.Button(self.buttons, text="Save", width= 15, command=self._on_save)
    self.savebutton.pack(side=tk.RIGHT, padx=3, pady=2)
    self.viewbutton = ttk.Button(self.buttons, text="View", width= 15, command=self._on_view)
    self.viewbutton.pack(side=tk.RIGHT, padx=3, pady=2)

    #entries
    self.label_frame = ttk.LabelFrame(self, text="Status Record", height= 200)
    self.label_frame.grid(sticky=tk.W + tk.E)
    self.status_label = ttk.Label(self.label_frame, text= "Welcome Movie Record")
    self.status_label.pack(side=tk.RIGHT)

  
    # in Application   self.recordform.bind('<<SaveRecord>>', self._on_save)
  def _on_delete(self):
    self.event_generate('<<DeleteRecord>>')
  def _on_reset(self):
    self.event_generate('<<ResetRecord>>')
  def _on_modify(self):
    self.event_generate('<<ModifyRecord>>')
  def _on_save(self):
    self.event_generate('<<SaveRecord>>')
  def _on_view(self):
    self.event_generate('<<ViewRecord>>')
