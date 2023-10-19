"""Q91.By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155]."""
def q91():
    nums = [12,24,35,24,88,120,155]
    return [num for num in nums[2:]]
# print(q91())

"""Q92.With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write
a program to make a list whose elements are intersection of the above
given lists."""
def q92():
    set1 = set ([1,3,6,78,35,55]) & set ([12,24,35,24,88,120,155])
    return set1
# print(q92())

"""Q93.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to
print this list after removing all duplicate values with original order
reserved."""
def q93():
    set_num = set([12,24,35,24,88,120,155,88,120,155])
    list_num = reversed(sorted(list(set_num)))
    return list(list_num)
# print(q93())

"""Q94.Define a class Person and its two child classes: Male and Female. All
classes have a method "getGender" which can print "Male" for Male class
and "Female" for Female class."""
class Person:
    def __init__(self, gender):
        self.gender = gender
        
    def getGender(self):
        print(self.gender)

class Male(Person):
    def __init__(self, gender):
        super().__init__(gender)
        
class Female(Person):
    def __init__(self, gender):
        super().__init__(gender)
        
m = Male("Male")
# m.getGender()
f = Female("Female")
# f.getGender()

import collections
"""Q95.Please write a program which count and print the numbers of each
character in a string input by console.
"""
""""
Python uses C-style string formatting to create new, 
formatted strings. The "%" operator is used to format a set of variables enclosed 
in a "tuple" (a fixed size list), together with a format string, 
which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".
"""
def q95():
    # user_input = input("Please enter: ")
    # print(collections.Counter(user_input))
    dic = {}
    str=input("Please Enter: ")
    for ch in str:
        dic[ch] = dic.get(ch,0)+1
    print("\n".join(["%s, %s" % (k,v) for k, v in dic.items()]))
# q95()
"""Q96.Please write a program which accepts a string from console and print it
in reverse order."""
def q96():
    str = input("Enter> ")
    print(str[::-1])
# q96()

"""Q97.Please write a program which accepts a string from console and print the
characters that have even indexes."""
def q97():
    str = input("Enter> ")
    print(str[::2])
# q97()
import itertools
"""Q98.Please write a program which prints all permutations of [1,2,3]"""

def permutations(elements):
    if len(elements) <= 1:
        yield elements
        return
    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            # nb elements[0:1] works in both string and list contexts
            yield perm[:i] + elements[0:1] + perm[i:]
            
def q98():
    lst = [1,2,3]
    # for num in lst:
    #     for n in lst:
    #         print(f"({num},{n})")
    print(list(itertools.permutations(lst)))
# q98()   
"""Q99.We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?"""
def q99():
    rabbit_foot=4
    chicken_foot=2
    head=35
    legs=94
    for r in range(head+1):
        c = head-r
        if((r*rabbit_foot + c*chicken_foot) == legs):
            print(f"r:{r}, c:{c}")
    
    


        

