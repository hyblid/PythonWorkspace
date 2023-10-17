"""Q71.Please write a program which accepts basic mathematic expression from
console and print the evaluation result."""
# expression = input("Please enter expression:")
# print(eval(expression))

"""Q72/73.Please write a binary search function which searches an item in a sorted
list. The function should return the index of element to be searched in
the list.(condition->sorted array)"""
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
arr = [ 2, 3, 4, 10, 40 ]
# print(binary_search(arr, 10))
"""Q74.Please generate a random float where the value is between 10 and 100
using Python math module."""
import random
# print(random.random() * 100)

"""Q75.Please generate a random float where the value is between 5 and 95 using
Python math module."""
# print(random.random() * 100-5)

"""Q76.Please write a program to output a random even number between 0 and 10
inclusive using random module and list comprehension."""
def even_generate():
    return [num for num in range(0,11) if num %2 ==0]
# print(random.choice(even_generate()))

"""Q77.Please write a program to output a random number, which is divisible by 5
and 7, between 0 and 10 inclusive using random module and list
comprehension"""
def generate():
    return [num for num in range(0,11) if num %5 ==0 and num %7 ==0]
# print(random.choice(generate()))

"""Q78.Please write a program to generate a list with 5 random numbers between
100 and 200 inclusive."""
numbers = random.sample(range(100,201), 5)
# print(numbers)

"""Q79.Please write a program to randomly generate a list with 5 even numbers
between 100 and 200 inclusive."""
numbers = random.sample([num for num in range(100,201) if num %2 ==0], 5)
# print(numbers)

"""Q80.Please write a program to randomly generate a list with 5 numbers, which
are divisible by 5 and 7 , between 1 and 1000 inclusive."""
numbers = random.sample([num for num in range(1,1000) if num %5 ==0 and num %7 ==0], 5)
print(numbers)