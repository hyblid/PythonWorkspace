import string

def mysum(*args):
    if not args:
        return args
    
    output = args[0]
    for item in args[1:]:
        output += item
    return output

def mysum_bigger_than(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

def sum_numeric(**items):
    sum = 0
    for num in items:
        if not isinstance(num, str):
           sum = sum + num 
    return sum

    output = {}

    for d in args:
        for key, value in d.items():
            if key in output:
                try:
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key], value]
            else:
                output[key] = value

    return output

def combine_dicts(*args):
    output = {}

    for d in args:
        for key, value in d.items():
            if key in output:
                try:
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key], value]
            else:
                output[key] = value

    return output


d = {"Firstname":"Sita", "Lastname":"Sharma", "Age":22, "Phone":1234567890}
print(combine_dicts(d))
     