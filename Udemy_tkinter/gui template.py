import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk

window = tk.Tk()
window.title("Demo")
window.geometry("600x400")

check1 = ttk.Checkbutton(window, text="Check1")
check2 = ttk.Checkbutton(window, text="Check2")
radio1 = ttk.Radiobutton(window, text="Radio1")
radio2 = ttk.Radiobutton(window, text="Radio1")
check1.pack()
check2.pack()
radio1.pack()
radio2.pack()


window.mainloop()