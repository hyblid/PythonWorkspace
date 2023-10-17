import time

def duration_decorator(func):
    def wrapper():
        print("Started time")
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f"durantion {duration}")
    return wrapper

def decorator(func):
    def wrapper():
        print("decorator begins")
        func()
        print("decorator ends")
    return wrapper

def double_decorator(func):
    def wrapper():
        func()
        func()
    return wrapper

@double_decorator     #first execute
@decorator            #second execute
@duration_decorator   #third execute 
def func():
    print("Function")
    time.sleep(1)

# func = duration_decorator(func)
# func = decorator(func)   
# func = double_decorator(func)
func()