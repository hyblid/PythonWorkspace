"""Q.3.1.a.Write function fib_rec(n) that recursively computes Fibonacci numbers based on the following definition"""
def fib_rec(n):
    if n <=2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    
fib_lambda = lambda x : 1 if x <=2 else fib_lambda(x-1) + fib_lambda(x-2)
# print(fib_lambda(6))
"""Q.3.1.b"""
def fib_itr(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1 or n == 2:
        return 1

    fib_n_2 = 1 #2nd last
    fib_n_1 = 1 #last

    for _ in range(2, n):
        result = fib_n_1 + fib_n_2
        fib_n_2 = fib_n_1
        fib_n_1 = result

    return result

def f(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        (a, b) = (b, a + b) #swap a=b, b=a+b
    return b

"""Q3.2.2a.Write recursive function count_digits(value) that finds the number of digits in a positive natural number.
We already discussed how to extract digits in the previous chapter in section 2.1."""
def count_digits(value):
    print(value)
    if value < 10:
        return 1
    else:
        return  count_digits(value//10) + 1 
# print(count_digits(245))
"""Q.3.2b.Calculate the sum of the digits of a number recursively. 
Write recursive function calc_sum_of_digits(value) for this purpose"""
def calc_sum_of_digits(value):
    if value < 10:
        return value
    else:
        remainder, last_digit = divmod(value, 10)
        return calc_sum_of_digits(remainder) + last_digit 
    
# print(calc_sum_of_digits(1234))

"""Q.3.3a.Create an iterative version for the GCD calculation."""
def gcd_itr(a, b):
    while b!= 0:
          a,b = b, a%b
    return a   
# print(gcd_itr(42,14))    
"""Q.3.b.Write function gcd(a, b) that computes the greatest common divisor (GCD) 
GCD can be expressed mathematically recursively as follows for two natural numbers a and b:"""
def gcd_rec(a, b):
    if b==0:
        return a
    else:
        return gcd_rec(b, a%b)
# print(gcd(42,28))

"""Q.3.c.Write function lcm(a, b) that computes the least common multiplier (LCM) . 
For two natural numbers a and b, you can calculate this based on the GCD using the following formula:
lcm(a,b) = a*b / gcd(a,b)"""
def lcm(a,b):
    return a * b / gcd_rec(a,b)
# print(lcm(42,14))

"""Q.3.4.Write recursive function reverse_string (text) that flips the letters of the text passed in."""
def reverse_string(input):
    if len(input) <= 1:
        return input
    first_char = input[0] #get value
    remaining = input[1:] #get value of list
    return reverse_string(remaining) + first_char
# print(reverse_string("123"))
"""Q.3.5.Write function sum_rec(values) that recursively 
computes the sum of the values of the given list. No call to the built-in functionality sum() is allowed."""
def sum_helper(values, pos):
    if pos >= len(values):
        return 0
    return values[pos] + sum_helper(values, pos+1)

def sum_rec(values):
    return sum_helper(values, 0)

# print(sum_rec([1,2,3]))
import sys
"""Q.3.5 Write function min_rec(values) that uses recursion to find the minimum value of the passed list. 
For an empty list, the value sys.maxsize should be returned."""
def min_helper(values, pos):
    if pos >= len(values):
        return sys.maxsize
    return values[pos] if values[pos] < min_helper(values, pos+1) else min_helper(values, pos+1)

def min_rec(values):
    return min_helper(values, 0)
    
print(min_rec([1, 2, 3, -7]))