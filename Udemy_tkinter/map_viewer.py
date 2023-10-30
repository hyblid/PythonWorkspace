import customtkinter as ctk
from resources.mapsettings import *
import tkintermapview
# import tkinter

class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		ctk.set_appearance_mode('light')
		self.geometry('1200x800+100+50')
		self.minsize(800,600)
		self.title('Map')
		# self.iconbitmap('map.ico')

		# layout 
		self.rowconfigure(0, weight = 1, uniform = 'a')
		self.columnconfigure(0, weight = 2, uniform = 'a')
		self.columnconfigure(1, weight = 8, uniform = 'a')

		# widgets 
		self.map_widgt = MapWidget(self)

		self.mainloop()

class MapWidget(tkintermapview.TkinterMapView):
	def __init__(self, parent):
		super().__init__(master = parent)
		self.grid(row = 0, column = 1, sticky = 'nsew')

		# # exercise:
		# # https://github.com/TomSchimansky/TkinterMapView
		# # use the documentation to update the map style to the terrain view
		# self.set_tile_server(TERRAIN_URL)

App()