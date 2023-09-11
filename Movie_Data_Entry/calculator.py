from tkinter import *

IVORY = "#FFE4C0"
PINK = "#FFBBBB"
BLUE = "#BFFFF0"
GREEN = "#BFFFF0"

window = Tk()
window.title("Calculator")
window.resizable(False,False)
window.config(padx=10, pady=10, bg=IVORY)

digits = [ ["7","8","9","*"],
          ["4","5","6","/"],
          ["1","2","3","-"],
          ["0",".","←","+"]
        ]

def clicked(digit):
    if digit == "←":
        input_entry.delete(len(input_entry.get())-1)
    else:
        input_entry.insert(END,digit)
        
def del_digit():
    input_entry.delete(0,END) 
    
def calculate():
    result = eval(input_entry.get())
    result_label.config(text=result)
    
input_entry = Entry(window, width=30, bg=IVORY, justify=RIGHT)
input_entry.grid(column=0, row=0, columnspan=4)
input_entry.focus()

result_label = Label(window, text= "test", width=2, bg=IVORY)
result_label.grid(column=0, row=1,columnspan=4, pady=15, padx=2)

for r in range(4):
    for c in range(4):
        digit = digits[r][c]
        button = Button(window, text=digit, width=8, bg=PINK, command= lambda x =digit: clicked(x))
        button.grid(column=c, row= r+2, pady=2, padx=2)
    
clear_button = Button(window, text="C", width=17,  bg=BLUE, command=del_digit)
clear_button.grid(column=0, row=6, columnspan=2, pady=5)
cal_button = Button(window, text="=", width=17, bg=BLUE, command=calculate)
cal_button.grid(column=2, row=6,columnspan=2, pady=5)
    
window.mainloop()    


