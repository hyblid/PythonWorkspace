import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")

def convert():
    print("Convert")


#title
title_label = ttk.Label(master=window, text="Miles to kilometers", font="Calibri 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left", pady=10)
input_frame.pack()
#output
out_label = ttk.Label(master=window, text="Output", font="Calibri 24 bold")
out_label.pack(pady=5)

#run 
window.mainloop()

