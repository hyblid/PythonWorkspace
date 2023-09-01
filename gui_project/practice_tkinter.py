from tkinter import *
from tkinter import ttk
import math as m
from Movie import *


movie_list = [Movie("Casablanca", 1942, 5),
              Movie("Wonde Woman", 2017, 4),
              Movie('Terminator', 1988, 5)]

def index_by_title(movie_list, title):
    index =0
    for movie in movie_list:
        if title == movie.title:
            print("matched index {}".format(index))
            return index
        else:
            index +=1 
    return -1 

print(index_by_title(movie_list, "Terminator"))

