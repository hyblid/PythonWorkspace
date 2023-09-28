#all items should be str
"""
all items should be add as string and it all affect 
from stuff import * - only import listed in __all__()    
"""

__all__ = ["a","c", "bar"]

a=1
b=2
c=3

def foo():
    return("invoked foo()")

def bar():
    return("invoked bar()")
