import random
"""Q81.Please write a program to randomly print a integer number between 7 and
15 inclusive."""
def q81():
    print(random.randrange(7,16))
# q81()

"""Q82.Please write a program to compress and decompress the string "hello
world!hello world!hello world!hello world!"."""
import zlib
def q82():
    s = ('hello world!hello world!hello world!hello world!').encode()
    t = zlib.compress(s)
    print(t)
    print (zlib.decompress(t))    
# q82()

import time
"""Q83.Please write a program to print the running time of execution of "1+1"
for 100 times."""
# def q83(): 
#     start = time.perf_counter()
#     for i in range (30):
#         sum = 1+1
#         time.sleep(1)
#     end = time.perf_counter()
#     print(end - start)
# q83()
"""Q84.Please write a program to shuffle and print the list [3,6,7,8]."""
def q84():
    lst = [3,6,7,8]
    random.shuffle(lst)
    print(lst)

"""Q85.Please write a program to generate all sentences where subject is in ["I",
"You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]."""
def q85():
    for subject in ["I", "You"]:
        for verb in ["Play", "Love"]:
            for obj in ["Hockey", "Football"]:
                print(f"{subject} {verb} {obj}")
# q85()
"""Q86.Please write a program to print the list after removing delete even
numbers in [5,6,77,45,22,12,24]."""
def q86():
    numbers = [5,6,77,45,22,12,24]
    return [num for num in numbers if num%2 ==0]
# print(q86())

"""Q87.By using list comprehension, please write a program to print the list
after removing delete numbers which are divisible by 5 and 7 in
[12,24,35,70,88,120,155]."""
def q87():
    lst = [12,24,35,70,88,120,155]
    return [num for num in lst if num%5 ==0 and num%7==0]
# print(q87())

"""Q88.By using list comprehension, please write a program to print the list
after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]."""
def q88():
    lst = [12,24,35,70,88,120,155]
    return [num for index, num in enumerate(lst) if index %2 != 0]
# print(q88())

"""Q89.By using list comprehension, please write a program generate a 3*5*8 3D
array whose each element is 0."""
def q89():
    return [[[0 for col in range(8)] for col in range(5)]for col in range(3)]
# print(q89())

"""Q90.By using list comprehension, please write a program to print the list
after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]."""
def q90():
    li = [12,24,35,70,88,120,155]
    li = [x for i,x in enumerate(li) if i not in (0,4,5)]
    print(li)
q90()    