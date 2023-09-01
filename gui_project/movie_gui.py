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

#movie_listBox Frame
frame_movieListBox = LabelFrame(root, text="Movie")
frame_movieListBox.pack(padx=10, pady=10, fill="both")
listbox = Listbox(frame_movieListBox, selectmode="extended", height=10)
listbox.pack(padx=15, pady=15, fill="both")

#Movie_details Frame
frame_movie_detial = LabelFrame(root, text="Movie Detail")
frame_movie_detial.pack(padx=10, pady=10,fill="both", ipadx=15)
# win.grid_columnconfigure((0,1,2), weight=1, uniform="column")

frame_content_title = Label(frame_movie_detial, text="Title").grid(column=0,row=0, sticky=E+W)
txt_stars = Entry(frame_movie_detial, width=25).grid(column=0, row=1, padx=30, pady=5, sticky=E+W)

frame_content_year = Label(frame_movie_detial, text="Year").grid(column=1,row=0, sticky=E+W)
txt_year = Entry(frame_movie_detial, width=25).grid(column=1,row=1, padx=15, pady=5, sticky=E+W)

frame_content_stars = Label(frame_movie_detial, text="Star").grid(column=2,row=0, sticky=E+W)
txt_title = Entry(frame_movie_detial, width=25).grid(column=2,row=1 , padx=15, pady=5, sticky=E+W)


#Function_deta1l Frame 
frame_function_detail = LabelFrame(root, text="Operations")
frame_function_detail.pack(padx=3, pady=3, ipadx=3, ipady=4)
#Button sfor de
btn_view = Button(frame_function_detail, text="VIEW", width=15, height=2).grid(column=0,row=0)
btn_add = Button(frame_function_detail, text="ADD",width=15, height=2).grid(column=1,row=0)
btn_delete = Button(frame_function_detail, text="DELETE",width=15, height=2, background='yellow').grid(column=2,row=0)
btn_modify = Button(frame_function_detail, text="MODIFY",width=15, height=2).grid(column=0,row=1)
btn_edit = Button(frame_function_detail, text="EDIT",width=15, height=2).grid(column=1,row=1)
btn_exit = Button(frame_function_detail, text="EXIT",width=15, height=2, background='red').grid(column=2,row=1)

movie_list = []


root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()



    