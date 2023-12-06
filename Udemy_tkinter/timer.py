import customtkinter as ctk
from resources.timer_settings import *
from tkinter import filedialog, Canvas

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BLACK)
        self.title("")
        self.geometry(f"300x600")
        self.resizable(False, False)
        ctk.set_appearance_mode(f'{"dark"}')
        self.iconbitmap(r"D:\test\PythonWorkspace\Udemy_tkinter\resources\empty.ico")
        #run app
        self.mainloop()
        
if __name__ == "__main__":
    App()    