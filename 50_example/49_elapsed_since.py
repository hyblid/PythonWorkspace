import time
import os
import glob

def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        #key is "or" operator return first 
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, item)
        
def elapsed_since_wait(data, min_wait):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)

        if delta < min_wait:
            time.sleep(min_wait - delta)

        last_time = time.perf_counter()
        yield (delta, item)
        
def file_usage_timing(dirname):
    for one_filename in os.listdir(dirname):
        full_filename = os.path.join(dirname, one_filename)

        yield (full_filename,
               os.stat(full_filename).st_mtime,
               os.stat(full_filename).st_ctime,
               os.stat(full_filename).st_atime)

def func(p):
    if p.isalpha():
        return p
    else: 
        return None

def yield_filter(data, func):
    for one_item in data:
        yield func(one_item)
           
data = ["1", "a", "2", "b"]  
print(list(yield_filter(data, func)))
