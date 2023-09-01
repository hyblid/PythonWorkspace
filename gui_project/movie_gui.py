from Movie import *
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Movie GUI")
root.geometry("640x480")
movie_list = [Movie("Casablancd", 1942, 5),
              Movie("Wonde Woman", 2017, 4),
              Movie('Terminator', 1988, 5)]

'''
main functions
'''
style = ttk.Style()
style.theme_use('clam')
tree = ttk.Treeview()

# Label Frame
frame_title = Frame(root, relief="solid", bd=1).pack()
label1 = Label(frame_title, text="Movie List", font=("Arial", 25))
label1.pack()

# movie_listBox Frame
frame_movieListBox = LabelFrame(root, text="Movie", height=200)
frame_movieListBox.pack(padx=10, pady=10, fill="both")

frame_movie_detial = LabelFrame(root, text="Movie Detail")
frame_movie_detial.pack(padx=10, pady=10, fill="both", ipadx=15)

txt_title = Entry(frame_movie_detial, width=25)
txt_year = Entry(frame_movie_detial, width=25)
txt_stars = Entry(frame_movie_detial, width=25)

tree = ttk.Treeview(frame_movieListBox,
                        column=("Title", "Year", "Stars"), show='headings', height=5)


def view_movie():
    # Add a Treeview widget
    global tree
    # Delete for refresh tree not duplicate s
    refresh_tree()
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Title")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Year")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Stars")

    # Insert the data in Treeview widget
    for movie in movie_list:
        tree.insert('', 'end', text="item",
                    values=(movie.title, movie.year, movie.stars))
    tree.bind("<Double-1>", OnDoubleClick)
    tree.pack()


def OnDoubleClick(event):
    global txt_title
    global txt_year
    global txt_stars
    # delete each entry values
    txt_title.delete(0, END)
    txt_year.delete(0, END)
    txt_stars.delete(0, END)
    # select row and get values
    current_item = tree.item(tree.focus())
    detail_item = list(current_item.get("values"))
    print("You clicked printed title:{0} year:{1} stars:{2}"
          .format(detail_item[0], detail_item[1], detail_item[2]))
    # insert values
    txt_title.insert(END, detail_item[0])
    txt_year.insert(END, detail_item[1])
    txt_stars.insert(END, detail_item[2])


def add_movie():    
    global txt_title
    global txt_year
    global txt_stars
    global movie_list
    # delete each entry values
    title = txt_title.get()
    year = txt_year.get()
    stars = txt_stars.get()
    if title != "" and year != "" and stars !="":
        movie_list.append(Movie(title, year, stars))
        print("Moive was added", movie_list)
        view_movie()
    else:
        print("Please enter entries")    
    
def refresh_tree():
    global tree
    tree.delete(*tree.get_children())
    # refresh screen
    root.update()
    

def modify_movie():
    global txt_title
    global txt_year
    global txt_stars
    global movie_list
    # delete each entry values
    title = txt_title.get()
    year = txt_year.get()
    stars = txt_stars.get()
    index = 0
    if title != " " and year != " " and stars !=" ":
        index = index_by_title(movie_list, title)
        if index != -1:    #update year
            movie_list[index].year = year
            movie_list[index].stars = stars
            print("Moive was modified", movie_list)
            view_movie()
    else:
        print("Please enter entries") 
    
    refresh_tree()
    view_movie()
    

def delete_movie():
    global txt_title
    global txt_year
    global txt_stars
    global movie_list
    # delete each entry values
    title = txt_title.get()
    year = txt_year.get()
    stars = txt_stars.get()
    index = 0
    if title != " " and year != " " and stars !=" ":
        index = index_by_title(movie_list, title)
        if index != -1:    #update year
            movie_list.pop(index)
            print("One record was deleted", movie_list)
    else:
        print("Please enter entries") 
    
    refresh_tree()
    view_movie()


def clear_movie():
    global txt_title
    global txt_year
    global txt_stars
    txt_title.delete(0, END)
    txt_year.delete(0, END)
    txt_stars.delete(0, END)
    
def index_by_title(movie_list, title):
    index =0
    for movie in movie_list:
        if title == movie.title:
            print("matched index {}".format(index))
            return index
        else:
            index +=1 
    return -1   

frame_content_title = Label(frame_movie_detial, text="Title").grid(
    column=0, row=0, sticky=E + W)
txt_title.grid(
    column=0, row=1, padx=35, pady=5, sticky=E + W)

frame_content_year = Label(frame_movie_detial, text="Year").grid(
    column=1, row=0, sticky=E + W)
txt_year.grid(
    column=1, row=1, padx=15, pady=5, sticky=E + W)

frame_content_stars = Label(frame_movie_detial, text="Stars").grid(
    column=2, row=0, sticky=E + W)
txt_stars.grid(column=2, row=1, padx=15, pady=5, sticky=E + W)


# Function_deta1l Frame
frame_function_detail = LabelFrame(root, text="Operations")
frame_function_detail.pack(padx=3, pady=3, ipadx=3, ipady=4)
# Buttons for details
btn_view = Button(frame_function_detail, text="VIEW",
                  width=10, height=2, command=view_movie).grid(column=0, row=0)
btn_add = Button(frame_function_detail, text="ADD",
                 width=10, height=2, command=add_movie).grid(column=1, row=0)
btn_modify = Button(frame_function_detail, text="MODIFY",
                    width=10, height=2, command=modify_movie).grid(column=2, row=0)
btn_clear = Button(frame_function_detail, text="CLEAR", width=10, height=2,
                   background="yellow", command=clear_movie).grid(column=3, row=0)
btn_delete = Button(frame_function_detail, text="DELETE", width=10, height=2,
                    background="yellow", command=delete_movie).grid(column=4, row=0)
btn_exit = Button(frame_function_detail, text="EXIT", width=10,
                  height=2, background="red", command=root.quit).grid(column=5, row=0)
root.resizable(False, True)  # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)


root.mainloop()
