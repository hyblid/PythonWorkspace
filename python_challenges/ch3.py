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
"""Q.3.6 Write function min_rec(values) that uses recursion to find the minimum value of the passed list. 
For an empty list, the value sys.maxsize should be returned."""
def min_helper(values, pos, min_value):
    if pos >= len(values):
        return min_value
    value = values[pos]
    if value < min_value:
        min_value = value
    return min_helper(values, pos + 1, min_value)

def min_rec(values):
    return min_helper(values, 0, sys.maxsize)
# print(min_rec([1, 2, 3, -7]))

"""Q.3.7.a.Write function to_binary(n) that recursively converts the given positive integer into 
a textual binary representation. No call to int(x, base) may be used."""
def to_binary(n):
    if n == 1:
        return str(n)
    remainder, last_digit = divmod(n, 2)
    return to_binary(remainder)  + str(last_digit)
# print(to_binary(7))

"""Q.3.7.b.Write conversions to octal and hexadecimal numbers by implementing 
the corresponding functions to_octal(n) and to_hex(n). Again, no call to int(x, base) may be used."""
def to_octal(n):
    if n < 8:
        return str(n)
    remainder, last_digit = divmod(n, 8)
    return to_octal(remainder)  + str(last_digit)
# print(to_octal(100))

def to_hex(n):
    if n == 0:
        return ""
    remainder, last_digit = divmod(n, 16)
    if 9 < last_digit <= 15: 
        last_digit =  chr(ord('A') + (last_digit - 10))
    return to_hex(remainder)  + str(last_digit)
# print(to_hex(15))
"""Q.3.8.a.Write recursive function is_power_of_2(n) that evaluates the given positive integer to see if it is a power of two."""
def is_power_of_2(n):
    if n <= 1:
        return True
    remainder, last_digit = divmod(n, 2)
    return  is_power_of_2(remainder) and last_digit == 0
# print(is_power_of_2(16))
        
"""Q.3.8.b. Write recursive function power_of(value, exponent) that exponentiates the given positive integer with the positive number 
specified as second parameter. For example, the call power_of(4, 2) should return the square of 4, so compute 42 = 16. You may not use the built-in functionality pow() or the operator **"""
def power_of_rec(value, exponent):
    if exponent == 0:
        return 1
    else:
        return power_of_rec(value, exponent - 1) * value
# print(power_of_rec(4,2))
    
"""Q.3.8.c. Write iterative function power_of(value, exponent) that exponentiates the given positive integer with the positive number 
specified as second parameter. For example, the call power_of(4, 2) should return the square of 4, so compute 42 = 16. You may not use the built-in functionality pow() or the operator **"""
def power_of_itr(value, exponent):
    sum = 1
    for _ in range(0, exponent):
        sum = sum * value
    return sum
# print(power_of_itr(4,2))

"""Q.3.2.9.Write function print_pascal(n) that prints Pascal’s triangle. For the value 5, the following output should be generated
n!/(n-r)!r!"""
def print_pascal(n):
    for i in range(1, n+1):
        C = 1
        for k in range(1, i+1):
    
            # first value in a line is always 1
            print(' ', C, sep='', end='')
    
            # using Binomial Coefficient
            C = C * (i - k) // k
        print()
# print_pascal(5)
"""Q.3.2.10.A palindrome is a word that reads the same from the front and the back. 
You can extend this definition to the digits of a number. 
Write recursive function is_number_palindrome(number) 
but without converting the number into a string and then using string functionalities like [::-1]."""
def is_number_palindrome_rec(number):
    return __is_number_palindrome_rec_helper(number, 0, number)

def __is_number_palindrome_rec_helper(original_number, current_value, remaining_value):
    if current_value == original_number:
        return True
    if (remaining_value < 1):
        return False
    last_digit = remaining_value % 10
    new_current = current_value * 10 + last_digit
    new_remaining = remaining_value // 10
    return __is_number_palindrome_rec_helper(original_number, new_current, new_remaining)

def reverse(number,reverse=0):
    while number > 0:
        remainder = number % 10
        number = number // 10
        reverse = (reverse * 10) + remainder
    return reverse

# print(is_number_palindrome_rec(17))

"""Q.3.2.11.Calculate all permutations of a sequence of letters given as a string; 
this means all possible combinations of these letters. 
Implement this calculation in function calc_permutations(text). Consider also the case of duplicate letters
, but do not use the standard Python functionality from the itertools module."""
def calc_permutations(input):
    if len(input) < 1:
        return {input}
    combinations = set()
    for i, new_first in enumerate(input):
        permutations = calc_permutations(input[0:i] + input[i + 1:])
        for perm in permutations:
            combinations.add(new_first + perm)
    return combinations
# print(calc_permutations("AAC"))
"""Q.3.2.12.Write function count_substrings (text, value_to_find) that counts all occurrences of the given 
substring. Thereby, when a pattern is found, it should be consumed; 
in other words, it should not be available for hits again. This is shown n the following table as the last case. 
Implement the whole thing yourself without resorting to the standard count()."""
def count_substrings (text, value_to_find):
    return count_substrings_helper(text, value_to_find)

def count_substrings_helper(text, value_to_find, count=0):
    index = text.find(value_to_find)
    if index == -1:
        return count
    else:
        return count_substrings_helper(text[index + len(value_to_find):], value_to_find, count + 1)
"""Q.3.2.13.In the introduction, I showed how to draw a simple shape of a ruler as well as 
a stylized snowflake (see Figure 3-3) using recursion. 
In this exercise, you want to imitate an English-style ruler. 
This involves dividing an area of one inch into 1/2 and 1/4 and 1/8. 
In doing so, the length of the strokes decreases by one each time."""