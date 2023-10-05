import os
import re
import glob


#path = "C:\\test\\PythonWorkspace\\Container"
def all_lines(path):
    for filename in os.listdir(path): #listdir just return file name
        full_filename = os.path.join(path,filename)
        try:
            for line in open(full_filename):
                yield line
        except OSError:
            pass

def all_lines_tuple(path):
    for file_index, filename in enumerate(os.listdir(path)): 
        full_filename = os.path.join(path,filename)
        try:
            for line_index, line in enumerate(open(full_filename)):
                yield (file_index, filename, line_index, line)
        except OSError:
            pass

def open_file_safely(filename):
    try:
        return open(filename)
    except OSError:
        return None


def all_lines_alt(path):
    all_files = [open_file_safely(os.path.join(path, filename))
                 for filename in os.listdir(path)]

    while all_files:
        for one_file in all_files:
            if one_file is None:
                all_files.remove(one_file)
                continue

            one_line = one_file.readline()

            if one_line:
                yield one_line
            else:
                all_files.remove(one_file)   
                
def all_lines(path, s):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                if s in line:
                    yield line
        except OSError:
            pass
        
        
                
line = list(all_lines("C:\\test\\PythonWorkspace\\Container"))
print(line)