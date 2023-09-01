from Movie import *
from tkinter import *

root = Tk()
root.title("Movie GUI")
root.geometry("640x480")

'''
main functions
'''

movie_list = [Movie(1, "Casablancd", 1942, 5),
       Movie(2,"Wonde Woman",2017, 4),
       Movie(3,'Terminator', 1988, 5)]

def view_movie():
    pass
def add_movie():
    pass
def modify_movie():
    pass
def delete_movie():
    pass

# Label Frame
frame_title = Frame(root, relief="solid", bd=1).pack()
label1 = Label(frame_title, text="Movie List", font=("Arial", 25))
label1.pack()

# movie_listBox Frame
frame_movieListBox = LabelFrame(root, text="Movie")
frame_movieListBox.pack(padx=10, pady=10, fill="both")
listbox = Listbox(frame_movieListBox, selectmode="extended", height=10)
listbox.pack(padx=15, pady=15, fill="both")

# Movie_details Frame
frame_movie_detial = LabelFrame(root, text="Movie Detail")
frame_movie_detial.pack(padx=10, pady=10, fill="both", ipadx=15)
# win.grid_columnconfigure((0,1,2), weight=1, uniform="column")

frame_content_title = Label(frame_movie_detial, text="Title").grid(
    column=0, row=0, sticky=E + W)
txt_stars = Entry(frame_movie_detial, width=25).grid(
    column=0, row=1, padx=35, pady=5, sticky=E + W)

frame_content_year = Label(frame_movie_detial, text="Year").grid(
    column=1, row=0, sticky=E + W)
txt_year = Entry(frame_movie_detial, width=25).grid(
    column=1, row=1, padx=15, pady=5, sticky=E + W)

frame_content_stars = Label(frame_movie_detial, text="Star").grid(
    column=2, row=0, sticky=E + W)
txt_title = Entry(frame_movie_detial, width=25).grid(
    column=2, row=1, padx=15, pady=5, sticky=E + W)


# Function_deta1l Frame
frame_function_detail = LabelFrame(root, text="Operations")
frame_function_detail.pack(padx=3, pady=3, ipadx=3, ipady=4)
# Buttons for details
btn_view = Button(frame_function_detail, text="VIEW",
                  width=15, height=2, command=view_movie).grid(column=0, row=0)
btn_add = Button(frame_function_detail, text="ADD",
                 width=15, height=2, command=add_movie).grid(column=1, row=0)
btn_modify = Button(frame_function_detail, text="MODIFY",
                    width=15, height=2, command=modify_movie).grid(column=2, row=0)
btn_delete = Button(frame_function_detail, text="DELETE"
                    , width=15, height=2, background="yellow", command=delete_movie).grid(column=3, row=0)
btn_exit = Button(frame_function_detail, text="EXIT", width=15,
                  height=2, background="red", command=root.quit).grid(column=4, row=0)
root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

print(movie_list)


root.mainloop()
