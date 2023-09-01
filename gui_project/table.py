from tkinter import *
from tkinter import ttk
from Movie import *

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')
movie_list = [Movie(1, "Casablancd", 1942, 5),
       Movie(2,"Wonde Woman",2017, 4),
       Movie(3,'Terminator', 1988, 5)]


# Add a Treeview widget
tree = ttk.Treeview(win, column=("Title", "Year", "Stars"), show='headings', height=5)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Title")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Year")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Stars")

for movie in movie_list:
# Insert the data in Treeview widget
    tree.insert('', 'end', text="1", values=(movie.title, movie.year, movie.stars))

tree.pack()

win.mainloop()