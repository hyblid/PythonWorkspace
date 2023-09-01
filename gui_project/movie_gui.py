"""
The Movie List Program
Commands
v-view
a-Add
d-Delete
m-modify
x-exit
Comman :v
   TTTLE      YEAR  STARS
1  xxx        1942   5     
2  xxx        2017   4
"""

from Movie import *
from tkinter import *

root = Tk()
root.title("Moive GUI")
root.geometry("640x480") 
#Label Frame
frame_title = Frame(root, relief="solid", bd=1).pack()
label1 = Label(frame_title, text="Movie List", font=("Arial", 25))
label1.pack()

#movie_list Frame
frame_movieList = LabelFrame(root, text="Movie")
frame_movieList.pack(fill="both")
listbox = Listbox(frame_movieList, selectmode="extended", height=0).pack()

#Movie_detail Frame
frame_movie_detial = LabelFrame(root, text="Movie Detail")
frame_movie_detial.pack(fill="both")

frame_content_title = LabelFrame(frame_movie_detial, text="Title")
frame_content_title.pack()
txt_stars = Entry(frame_content_title).pack(side="right")

frame_content_year = LabelFrame(frame_movie_detial, text="Year")
frame_content_year.pack()
txt_year = Entry(frame_content_year).pack(side="right")

frame_content_stars = LabelFrame(frame_movie_detial, text="Star")
frame_content_stars.pack()
txt_title = Entry(frame_content_stars).pack(side="right")

#Function_deta1l Frame 
frame_function_detail1 = LabelFrame(root, text="Operation")
frame_function_detail1.pack()
btn_view = Button(frame_function_detail1, text="VIEW")
btn_view.pack(side="right")
btn_add = Button(frame_function_detail1, text="ADD")
btn_add.pack(side="right")
btn_delete = Button(frame_function_detail1, text="DELETE")
btn_delete.pack(side="right") 
btn_modify = Button(frame_function_detail1, text="MODIFY")
btn_modify.pack(side="right")
btn_edit = Button(frame_function_detail1, text="EDIT")
btn_edit.pack(side="right")
btn_exit = Button(frame_function_detail1, text="EXIT")
btn_exit.pack(side="right")




movie_list = []

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()



    