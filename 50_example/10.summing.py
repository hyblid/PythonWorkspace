import string

def mysum(*args):
    if not args:
        return args
    
    output = args[0]
    for item in args[1:]:
        output += item
    return output
# print(mysum(1,2,3,4,5,6,7,8,9,10))
"""only first argument become threshold and others *args
"""
def mysum_bigger_than(threshold, *items):
    if not items:
        return items
    output = 0
    for item in items:
        if item > threshold:
            output += item
    return output

# print(mysum_bigger_than(10, 5, 20, 30, 6))

""" sum_numeric(10, 20, 'a', '30','bcd') --> arg"""
def sum_numeric(*items):
    total = 0
    for item in items:
        try:
            total += int(item)
        except ValueError:
            pass
    return total
# print(sum_numeric(10, 20, 'a', '30','bcd'))

def combine_dicts(dict_list): #should be not *arg, **kwarg
    output = {}

    for d in dict_list:
        for key, value in d.items():
            if key in output:
                try:
                    output[key].append(value)
                except:
                    output[key] = [output[key], value]
            else:
                output[key] = value
    return output

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
dict3 = {'e': 7}
list_of_dicts = [dict1, dict2, dict3]
print(combine_dicts(list_of_dicts))

     