"""
*args - tuple, **kwargs - ditionary
"""

def test(first, *args, **kwargs):
    print(first)
    print(args)
    print(kwargs)
    
def test1(first, *args, rest):
    print(first)
    print(args)
    print(rest)    

test(1,2,3,4,5,6, name="howard", age=1)
"""
1
(2, 3, 4, 5, 6)
{'name': 'howard', 'age': 1}
"""
test(1,2,3,4,5)
"""
1
(2, 3, 4, 5)
{}
"""

#unpacking parameters and unpacking list
first, *args, third = [1,2,3,4,5,6,7,8,9]
print(f"first:{first}")
print(f"args:{args}")
print(f"third:{third}")

config = {"sever":"localhost",
          "port":3306, 
          "user":"root",
          "password":"Py1thon!Xt12"}

def connect(**kwargs):
    print(kwargs)

connect(**config)

#connect(config) Error : connect() takes 0 positional arguments but 1 was given
    
    