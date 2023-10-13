import math
"""Q51.Define a class named American and its subclass NewYorker."""
class American:
    def __init__(self, name, age):
        self.name = name
        self.name = age

class NewYorker(American):
    def __init__(self, name, age, address):
        self.address = address
        super().__init__(name, age)
        
# n = NewYorker("Howard", 55, "2562 willowburne DR")
# print(n.name)

"""Q52.Define a class named Circle which can be constructed by a radius. The
Circle class has a method which can compute the area."""
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def cal_area(self):
        return round(math.pi * pow(self.radius,2),2)  
# c = Circle(5)
# print(c.cal_area())

"""Q53.Define a class named Rectangle which can be constructed by a length and
width. The Rectangle class has a method which can compute the area.""" 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def cal_area(self):
        return round(self.length * self.width ,2)
# r = Rectangle(5, 10)
# print(r.cal_area())

"""Q54.Define a class named Shape and its subclass Square. The Square class has
an init function which takes a length as argument. Both classes have a
area function which can print the area of the shape where Shape's area is
0 by default."""
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Squre(Shape):
    def __init__(self, length):
        self.length = length
        # Shape.__init__(self)
        super().__init__()
        
    def area(self):
        return self.length * self.length
# s = Squre(6)
# print(s.area())

"""Q55.Please raise a RuntimeError exception."""
# raise RuntimeError("Runtime error has been occured")        
       
"""Q56.Write a function to compute 5/0 and use try/except to catch the
exceptions."""
def throws():
    return 5/0

# try:
#     throws()
# except ZeroDivisionError:
#     print("Zero Division Error")
# except Exception:
#     print("Exception catched")
# finally:
#     print("In finally block for cleanup")

"""Q57.Define a custom exception class which takes a string message as attribute."""

class MyError(Exception):
    def __init__(self,message):
        self.message = message
        
error = MyError("custome Error!!!!!!!")
# print(error.message)

"""Q58 + Q59.Assuming that we have some email addresses in the
"username@companyname.com" format, please write program to print the user
name of a given email address. Both user names and company names are
composed of letters only."""
import re
emailAddress = "hwang_hoyoen@hotmail.com"
pat2 = "(\w+)@(\w+)+(\.com)"
r2 = re.match(pat2,emailAddress)
# print(r2.group(1), r2.group(2))

"""Q60.Write a program which accepts a sequence of words separated by whitespace
as input to print the words composed of digits only."""
user_input = "word happy 1111 girl boy 1boy 2 girl"
print(re.findall("\d+",user_input))

 