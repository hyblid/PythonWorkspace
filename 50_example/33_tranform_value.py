import os
import glob

d = {'a':1, 'b':2, 'c':3, 'd':4}

def transform_values(func, a_dict):
    return {key: func(value) for key, value in a_dict.items()}

def transform_values2(func1, func2, a_dict):
    return {key: func1(value) for key, value in a_dict.items() if func2(key, value)}

def first(value):
    return value * 2 

def second(key, value):
    flag = False
    if value % 2 == 0 and key.isalpha():
       flag = True
    return flag

def transform_values3(dict):
    return {record.split(":")[0] : record.split(":")[2] for record in open("passwd.txt")}
    """Write a function that takes a directory name (i.e., a string) as an argument. The
function should return a dict in which the keys are the names of files in that
directory, and the values are the file sizes. You can use os.listdir or glob
.glob to get the files, but because only regular files have sizes, you’ll want to filter
the results using methods from os.path. To determine the file size, you can
use os.stat or (if you prefer) just check the length of the string resulting from
reading the file.
    """
def transform_value4(dirname):
    return {one_filename: os.stat(one_filename).st_size
            for one_filename in glob.glob(f'{dirname}/*')
            if os.path.isfile(one_filename)}
    
print(transform_value4("Container"))
