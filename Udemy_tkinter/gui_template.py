import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk

window = tk.Tk()
window.title("Demo")
window.geometry("600x400")

#window minimum
window.minsize(200, 100)

# screen attributes 
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# security event 
window.bind('<Escape>', lambda event: window.quit())




window.mainloop()