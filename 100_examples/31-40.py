"""Q31.Define a function that can accept two strings as input and print the
string with maximum length in console. If two strings have the same
length, then the function should print all strings line by line."""
def q31():
    user_input = input("Enter two stirngs: ").split(" ")
    if len(user_input[0]) > len(user_input[1]):
        print(user_input[0])
    elif len(user_input[0]) < len(user_input[1]):
        print(user_input[1])
    elif len(user_input[0]) == len(user_input[1]):
        print(user_input[0] + user_input[1])
# q31()
"""Q32.Define a function that can accept an integer number as input and print
the "It is an even number" if the number is even, otherwise print "It is
an odd number".
"""
def q32():
    user_input = int(input("Enter number: "))
    if user_input % 2 ==0:
        print("It is an even number")
    else: 
        print("It is an odd number")
# q32()

"""Q33.Define a function which can print a dictionary where the keys are numbers
between 1 and 3 (both included) and the values are square of keys.
"""
dict = { 1: "one", 2:"two", 3:"three", 4: "four", 5: "five"}
def q33(dict):
    for key in dict.keys():
        if 1 <= key <= 3:
            print(pow(key, 2))
# q33(dict)

"""Q34.Define a function which can print a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys."""
dict1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
         11:"eleven", 12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
         19:"nineteen",20:"twenty",21:"twentyone", 22:"twentytow"}
def q34(dict):
    for key in dict.keys():
        if 1 <= key <= 20:
            print(pow(key, 2))
# q34(dict1)

"""Q35+Q36.Define a function which can generate a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of
keys. The function should just print the values only."""
def q35():
        dict3 = {}
        for i in range(1,21):
            dict3[i] = pow(2,i)
        for value in dict3.values():
            print(value)
#q35()

"""Q37.Define a function which can generate and print a list where the values
are square of numbers between 1 and 20 (both included)."""
def q37():
    return [pow(num, 2) for num in range(1,21)]
# print(q37())

"""Q38.Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to
print the first 5 elements in the list."""
def q38():
    lst = [pow(num, 2) for num in range(1,21)]
    print(lst[:5])
# q38()

"""Q39.Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to
print the last 5 elements in the list."""
def q39():
    lst = [pow(num, 2) for num in range(1,21)]
    print(lst[-5:])
# q39()   

"""Q40.Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to
print all values except the first 5 elements in the list.""" 
def q40():
    lst = [pow(num, 2) for num in range(1,21)]
    print(lst[5:])
# q40()
