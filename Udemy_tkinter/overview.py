import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

#window - change form tk.Tk()
window = ttk.Window(themename="journal")
window.title("Demo")
window.geometry("300x150")

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)
"""
tk.StringVar(): This holds characters like a Python string.
tk.IntVar(): This holds an integer value.
tk.DoubleVar(): This holds a double value (a number with a decimal place).
tk.BooleanVar(): This holds a Boolean to act like a flag.
"""
#title
title_label = ttk.Label(master=window, text="Miles to kilometers", font="Calibri 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left", pady=10)
input_frame.pack()
#output
output_string = tk.StringVar()
out_label = ttk.Label(
    master=window, 
    text="Output", 
    font="Calibri 24 bold", 
    textvariable=output_string)
out_label.pack(pady=5)

#run 
window.mainloop()