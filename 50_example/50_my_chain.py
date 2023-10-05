from itertools import chain
import os

def mychain(*args):
    for arg in args:
        for item in arg:
            yield item
# for x in mychain("abc", [1,2,3], {"a":1, "b":2}):
#     print(x)

def myzip(*args):
    # min(args, key=len) --> get min value by length
    for i in range(len(min(args, key=len))):
        yield tuple(one_arg[i] for one_arg in args)        
        
# print(list(myzip('abc', [10, 20, 30])))
    
path = "C:\\test\\PythonWorkspace\\Container"
def all_lines(path):
    #get ready value for args
    return mychain(*(open(os.path.join(path,filename)) 
              for filename in os.listdir(path) 
              if os.path.isfile(os.path.join(path,filename))))

def myrange(first, second=None, step=1):
    if second is None:
        current = 0
        stop = first
    else:
        current = first
        stop = second

    while current < stop:
        yield current
        current += step
        
print(list(myrange(5)))    