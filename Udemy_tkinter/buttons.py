from customtkinter import CTkButton
from settings import *
import resources.calculator_settings as setting

class Button(CTkButton):
    def __init__(self, parent, text,func, col, row, font, span = 1, color="dark-gray"):
        super().__init__(master=parent,
                         command=func, 
                         text=text,
                         corner_radius=setting.STYLING["corner-radius"],
                         font = font,
                         fg_color = setting.COLORS[color]["fg"],
                         hover_color= setting.COLORS[color]["hover"],
                         text_color = setting.COLORS[color]["text"])
        self.grid(column=col, columnspan = span, row=row, sticky="news", padx = setting.STYLING["gap"],pady = setting.STYLING["gap"])
        
class NumButton(Button):
    def __init__(self, parent , text, func, col, row, font, span, color="light-gray"):
        super().__init__(parent = parent, 
                         text = text, 
                         func = lambda:func(text), 
                         col = col, 
                         row = row, 
                         font = font, 
                         color = color,
                         span = span)
        
        



class MathButton(Button):
    def __init__(self, parent , text, operator, func, col, row, font, color="orange"):
        super().__init__(parent = parent, 
                         text = text, 
                         func = lambda:func(operator), 
                         col = col, 
                         row = row, 
                         font = font, 
                         color = color)  
        
class ImageButton(CTkButton):
    def __init__(self, parent, func, col, row, image, text = "",color="dark-gray"):
        super().__init__(master=parent,
                         command=func, 
                         text=text,
                         corner_radius=setting.STYLING["corner-radius"],
                         image = image,
                         fg_color = setting.COLORS[color]["fg"],
                         hover_color= setting.COLORS[color]["hover"],
                         text_color = setting.COLORS[color]["text"])
        self.grid(column=col, row=row, sticky="news", padx = setting.STYLING["gap"],pady = setting.STYLING["gap"])         
    
class MathImageButton(ImageButton):
    def __init__(self, parent, operator, func, col, row, image, color="orange"):
        super().__init__(parent = parent, 
                         func = lambda:func(operator), 
                         col = col, 
                         row = row, 
                         image = image, 
                         color = color)    
