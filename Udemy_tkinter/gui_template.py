import customtkinter as ctk

window = ctk.CTk()
window.title("Demo")
window.geometry("600x400")

#window minimum
window.minsize(200, 100)

# screen attributes 
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# security event 
window.bind('<Escape>', lambda event: window.quit())
button = ctk.CTkButton(window, text="Button")
button.pack()



window.mainloop()