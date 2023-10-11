print((lambda x: x+10)(3))

""" lambda function is anoumous fumction so give a nema"""
a = lambda x: x+10
print(a(10))

def build_quadratic_functions(a,b,c):
    """returns the fuction f(x)= ax^2 + bx +c"""
    return lambda x: a*x**2 + b*x +c
build_quadratic_functions(3,0,1)(2)

"""use lambda with built in functions
   sort, sorted, map, filter, reduce.....
"""