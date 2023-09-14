from collections import *


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}


def dictdiff1(first, second):
    output= {}
    all_keys = first.keys() | second.keys()
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output

def multi_update(*args):
    output = {}
    for one_dict in args:
        output.update(one_dict)
    return output

def dict_from_list(*args):
    if len(args) % 2:
        raise ValueError('Need an even number of args')
    output = {}
    while args:
        output[args[0]] = args[1]
        args = args[2:]
    return output

def partition_dict(d, f):
    output_true = {}
    output_false = {}

    for key, value in d.items():
        if f(key, value):
            output_true[key] = value
        else:
            output_false[key] = value
    return output_true, output_false   
    
print(dict_partition(d1, 1))

