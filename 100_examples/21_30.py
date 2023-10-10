"""Q21.A robot moves in a plane starting from the original point (0,0). The
robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The
trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡-
The numbers after the direction are steps. Please write a program to
compute the distance from current position after a sequence of movement
and original point. If the distance is a float, then just print the
nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3 --> y:2
LEFT 3
RIGHT 2 --> y:-1
Then, the output of the program should be:
2    √(2 - 0)2 + (-1 - 0)2"""
import math

def q21():
    x_0=0
    x_1=0
    y_0=0
    y_1=0
    
    while True:
        try:
            information = input("Enter or Ctrl-Z>").split(" ")
        except EOFError:
            break
        
        if information[0] == "UP":
            y_1 += int(information[1])
        elif information[0] == "DOWN":
            y_1 += int(information[1])
        elif information[0] == "WEST":
            x_1 += int(information[1])
        elif information[0] == "EAST":
            x_1 += int(information[1])
    distance = int(math.sqrt((x_1 - x_0)+(y_1 - y_0)))
    print(distance)
# q21()
"""Q22.Write a program to compute the frequency of the words from the input. The
output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1"""
from collections import Counter
def q22():
    information = sorted(input("Enter or Ctrl-Z>").split(" "))
    return {item : (information.count(item)) for item in information}
# print(q22())

"""Q23.Question: Write a method which can calculate square value of number"""
def q23():
    for num in range(0,50):
        print(math.pow(num,2), end=",")
# q23()
"""Q24.Python has many built-in functions, and if you do not know how to use
it, you can read document online or find some books. But Python has a
built-in document function for every built-in functions.
Please write a program to print some Python built-in functions
documents, such as abs(), int(), raw_input()
And add document for your own function"""
def q24():
    print(int.__doc__)
# q24()

"""Q25.Define a class, which have a class parameter and have a same instance
parameter.
class q25:
   x=0 ---> class attribute and this one does not need self.
            try to access q25.xxx
"""
class q25:
    #class attribute, and every instance has attribute as global
    name="Howard"
    def __init__(self, name=None):
        #instance attribute
        self.name= "Sakazaki" 

# jeffrey = q25("Jeffrey")
# print ("%s name is %s" % (q25.name, jeffrey.name))
# nico = q25()
# nico.name = "Nico"
# print ("%s name is %s" % (q25.name, nico.name))
"""Q26.Define a function which can compute the sum of two numbers."""
def q26(num1, num2):
    return num1 + num2
"""Q27.Define a function that can convert a integer into a string and print it in console."""
def q27(str):
    print(chr(str))
# q27(65)

"""Q28.Define a function that can convert a integer into a string and print it in console."""
def q28(str):
    print(chr(str))
"""Q29.Define a function that can receive two integral numbers in string form
and compute their sum and then print it in console."""
def q29():
    user_input = input("Enter two number: ").split(" ")
    return int(user_input[0]) + int(user_input[1])

# print(q29())

"""Q30.Define a function that can accept two strings as input and concatenate
them and then print it in console."""
def q30():
    user_input = input("Enter two strings: ").split(" ")
    return user_input[0] + user_input[1]
# print(q30())