import tkinter as tk
from tkinter import ttk
from datetime import datetime
from .constants import FieldTypes as FT
from . import widgets as w
"""
View has widgets
"""

class DataRecordForm(tk.Frame):
  """The input form for our widgets"""

  var_types = {
    FT.string: tk.StringVar,
  }

  def _add_frame(self, label, cols=3):
    """Add a labelframe to the form"""

    frame = ttk.LabelFrame(self, text=label)
    frame.grid(sticky=tk.W + tk.E)
    for i in range(cols):
      frame.columnconfigure(i, weight=1)
    return frame

  def __init__(self, parent, model, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    self.model= model
    fields = self.model.fields

    # Create a dict to keep track of input widgets
    self._vars = {
      key: self.var_types[spec['type']]()
      for key, spec in fields.items()
    }

    # Build the form
    self.columnconfigure(0, weight=1)

    # Record info section
    r_info = self._add_frame("Record Information")

    # line 1
    w.LabelInput(
      r_info, "Title",
      field_spec=fields['Title'],
      var=self._vars['Title'],
    ).grid(row=0, column=0)
    w.LabelInput(
      r_info, "Year",
      field_spec=fields['Year'],
      var=self._vars['Year'],
    ).grid(row=0, column=1)
    w.LabelInput(
      r_info, "Stars",
      field_spec=fields['Stars'],
      var=self._vars['Stars'],
    ).grid(row=0, column=2)
 
    #buttons
    buttons = tk.LabelFrame(self, text="Operations")
    buttons.grid(sticky=tk.W + tk.E)
    self.savebutton = ttk.Button(
      buttons, text="Save")
    self.savebutton.pack(side=tk.RIGHT)

    self.resetbutton = ttk.Button(
      buttons, text="Reset")
    self.resetbutton.pack(side=tk.RIGHT)

    # # default the form
    # self.reset()