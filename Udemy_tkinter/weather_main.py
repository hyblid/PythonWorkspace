import customtkinter as ctk
from resources.weather_settings import *
from main_widgets import *
#url request
import urllib.request
import json
from weather_data import get_weather
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass
#2ee92afc35fe6c6cf61f155e13b836e4

class App(ctk.CTk):
    def __init__(self, current_data, forecast_data, city, country):
        #data 
        self.current_data = current_data
        self.forecast_data = forecast_data
        self.location = {"city":city, "country":country}
        self.color = WEATHER_DATA[current_data["weather"]]
        
        super().__init__(fg_color= self.color["main"])
        self.title_bar_color(self.color["title"])
        self.geometry("550x250")
        self.minsize(550,250)
        self.title("")
        self.iconbitmap(r"D:\test\PythonWorkspace\Udemy_tkinter\resources\empty.ico")
        ctk.set_appearance_mode(f'{"dark"}')
        
        #small widget
        self.widget = SmallWidget(self, self.current_data, self.location, self.color)
        
        
        #states
        self.height_break = 600
        self.width_break = 1000
        self.full_height_bool = ctk.BooleanVar(value = False) 
        self.full_width_bool = ctk.BooleanVar(value = False)
        self.bind("<Configure>", self.check_size) 
        self.full_width_bool.trace("w", self.change_size)
        self.full_height_bool.trace("w", self.change_size)
        self.mainloop()
        
    def title_bar_color(self, color):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = color
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass

    def check_size(self,event):
        #only check only main window 
        if event.widget == self:
            # width
            if self.full_width_bool.get():
                if event.width < self.width_break:
                    self.full_width_bool.set(False)
            else:
                if event.width > self.width_break:
                    self.full_width_bool.set(True)
            # height
            if self.full_height_bool.get():
                if event.height < self.height_break:
                    self.full_height_bool.set(False)
            else:
                if event.height > self.height_break:
                    self.full_height_bool.set(True)
    
    def change_size(self, *arg):
        #remove previous window
        self.widget.pack_forget()
        
        #max widget
        if self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = MaxWidget(self)
        #tall widget
        if self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = TallWidget(self)
        #wide widget
        if not self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = WideWidget(self)
        #min widget    
        if not self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = SmallWidget(self)

if __name__ == '__main__':
    #location
    with urllib.request.urlopen("https://ipapi.co/json/") as url:
        data = json.loads(url.read().decode())
        # city = data["city"]
        # country = data["country_name"]
        # latitude = data["latitude"]
        # longitude = data["longitude"]
        city = "London"
        country = "United Kingdom"
        latitude = 51.5
        longitude = 0.13
        
    #weather information
    current_data = get_weather(latitude, longitude, "metric", "today")
    forecast_data = get_weather(latitude, longitude, "metric", "forecast")
    
    App(current_data = current_data, 
        forecast_data = forecast_data,
        city = city,
        country = country)