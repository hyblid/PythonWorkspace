import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk

window = tk.Tk()
window.title("Demo")
window.geometry("600x400")

#window minimum
window.minsize(200, 100)
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
"""  side = top or bottom                 |         side= left or right
   widget canb e as wide as the container |widget canb e as height as the container
   expand determines height               |expand determines the width 
"""
#exapnd : Determines how much space a widget can occupy only in 1 direction!
#- Width no set by expand if "side" is top or bottom (it already expanded for width)
#- Height is set by expand but only vertically!
#fill : Sets how much space the widget will occupy (x,y,both,None)
#side : determines the direction of the widgets
label1.pack(side="left", expand= True, fill="y")
label2.pack(side="left",  expand= True, fill="both")

window.columnconfigure(0, weight =1) # weight is wide
window.columnconfigure(1, weight =1)
window.columnconfigure(2, weight =2)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

label1.grid(row=0, column=1, sticky="nsew") #stick with 4 directions border
label2.grid(row=1, column=1, columnspan =2, sticky="nsew")
 



# screen attributes 
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# security event 
window.bind('<Escape>', lambda event: window.quit())




window.mainloop()