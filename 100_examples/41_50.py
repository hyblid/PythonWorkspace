"""Q41.Define a function which can generate and print a tuple where the value
are square of numbers between 1 and 20 (both included).
"""
def q41():
    return tuple(pow(num,2) for num in range(1,21))
# print(q41())

"""Q42.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
first half values in one line and the last half values in one line."""
def q42():
    t = (1,2,3,4,5,6,7,8,9,10)
    half = int(len(t)/2)
    print(t[:half])
    print(t[half:])
# q42()

"""Q43.Write a program to generate and print another tuple whose values are even
numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)."""
def q43():
    t=(1,2,3,4,5,6,7,8,9,10)
    even =()
    for num in t:
        if num % 2 == 0:
            even += (num,)
    return even
# print(q43())

"""Q44.Write a program which accepts a string as input to print "Yes" if the
string is "yes" or "YES" or "Yes", otherwise print "No". yES,yeS,YEs"""
def q44():
    user_input = input("Please enter: ")
    if user_input.islower() or user_input.isupper() or user_input.istitle():
        print("Yes")
    else:
        print("No")
# q44()

"""Q45.Write a program which can filter even numbers in a list by using filter
function. The list is: [1,2,3,4,5,6,7,8,9,10]."""
def q45():
    lst = [1,2,3,4,5,6,7,8,9,10]
    return list(filter(lambda x: (x %2 ==0), lst))
# print(q45())
              
            
"""Q46.Write a program which can map() to make a list whose elements are square
of elements in [1,2,3,4,5,6,7,8,9,10]."""
def q46():
    lst = [1,2,3,4,5,6,7,8,9,10]
    return list(map(lambda x : pow(x,2), lst))
# print(q46())

"""Q47.Write a program which can map() and filter() to make a list whose
elements are square of even number in [1,2,3,4,5,6,7,8,9,10]."""
def q47():
    lst = [1,2,3,4,5,6,7,8,9,10]
    return list(filter(lambda x: (x % 2 ==0), map(lambda x : pow(x,2), lst)))
# print(q47()) 
"""Q48.Write a program which can filter() to make a list whose elements are even
number between 1 and 20 (both included)."""
def q48():
    return list(filter(lambda x: (x % 2 ==0), range(1,21)))
# print(q48())

"""Q49.Write a program which can map() to make a list whose elements are square
of numbers between 1 and 20 (both included)."""
def q49():
    return list(filter(lambda x: (x % 2 ==0), range(1,21)))
# print(q49())

"""Q50.Define a class named American which has a static method called
printNationality."""
class American:
    @staticmethod
    def print_nationality():
        print("American")
# American.print_nationality()

    
