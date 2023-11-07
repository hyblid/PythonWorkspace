import numpy as np
from enum import Enum, auto
from array_utils import get_dimension, swap, print_array 

numbers= [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

"""Q.5.2.1.Write function order_even_before_odd(numbers). 
This is supposed to rearrange a given array or a list of int values so that the even numbers appear first, 
followed by the odd numbers. The order within the even and odd numbers is not of relevance."""

def order_even_before_odd(numbers):
    arr = np.array(numbers)
    index = 0
    for i in np.arange(len(arr)):
        if arr[i] % 2 ==0:
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp
    return arr    
# print(order_even_before_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(order_even_before_odd([2, 4, 6, 1, 8]))
# print(order_even_before_odd([1, 3, 2, 6, 5]))

"""Q.5.2.2.Write generic functions for flipping a two-dimensional array horizontally with flip_horizontally(values2dim) 
and vertically with flip_vertically(values2dim). 
The array should be rectangular, so no line should be longer than another.
flip_horizontally()     flip_vertically()
-------------------     -----------------
123      321           123      789
456  =>  654           456  =>  456
789      987           789      123"""

dim1 = [[1,2,3],[4,5,6],[7,8,9]]
class Rotate_Direction(Enum):
    LEFT = auto()
    RIGHT = auto()

def flip_horizontally(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for y in range(max_y):
        left_idx = 0
        right_idx = max_x - 1
        while left_idx < right_idx:
            left_value = values2dim[y][left_idx]
            right_value = values2dim[y][right_idx]
            values2dim[y][left_idx] = right_value
            values2dim[y][right_idx] = left_value
            left_idx += 1
            right_idx -= 1

def flip_vertically(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for x in range(max_x): 
        top_idx = 0
        bottom_idx = max_x - 1
        while top_idx < bottom_idx:
            top_idx = values2dim[top_idx][x]
            bottom_idx = values2dim[bottom_idx][x]
            values2dim[top_idx][x] = bottom_idx
            values2dim[bottom_idx][x] = top_idx
            top_idx += 1
            bottom_idx -= 1
            
def flip_horizontally_v2(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for y in range(max_y):
        row = values2dim[y]
        for x in range(max_x // 2):
            swap(row, x, max_x - x - 1)      

def flip_vertically_v2(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for x in range(max_x):
        col = values2dim[x]
        # for y in range(max_y // 2):
        #     swap(col, y, max_y - y - 1)                    
# flip_vertically_v2(dim1)
# print(dim1)
"""Q.5.2.3.Write function is_palindrome(values) that checks an array of strings for whether its values form a palindrome.
[“One”, “Test”, “ – ”, “Test”, “One”]
[“Max”, “Mike”, “Mike”, “Max”]
[“Tim”, “Tom”, “Mike”, “Max”]
"""
def is_palidrome(value):
    left = 0
    right = len(value)-1
    while left < right:
        if value[left] != value[right]:
            return False
        left += 1
        right -=1
    return True
        
# print(is_palidrome(["One", "Test", "–", "Test", "One"]))        
# print(is_palidrome(["Tim", "Tom", "Mike", "Max"]))        
# print(is_palidrome(["Max", "Mike", "Mike", "Max"]))        

"""Q.5.2.4.In the introductory section, I showed how to rotate arrays. 
Now try this inplace without creating a new array. 
Your task is to rotate a two-dimensional, square-shaped array by 90 degrees clockwise. 
Write generic function rotate_inplace(values2dim) that iteratively implements this."""
class RotationDirection(Enum):
    LEFT_90 = auto()
    RIGHT_90 = auto()
    
values = [
        ['1', '2', '3', '4', '5', '6'],
        ['J', 'K', 'L', 'M', 'N', '7'],
        ['I', 'V', 'W', 'X', 'O', '8'],
        ['H', 'U', 'Z', 'Y', 'P', '9'],
        ['G', 'T', 'S', 'R', 'Q', '0'],
        ['F', 'E', 'D', 'C', 'B', 'A']]
    
def rotate_inplace(values2dim):
    max_y, max_x = get_dimension(values2dim)
    height = max_y - 1
    width = max_x - 1
    offset = 0
    while offset <= width // 2:
        current_width = width - offset * 2
        for idx in range(current_width):
            # top, right, bottom, left
            lo_x = offset + idx
            lo_y = offset
            ro_x = width - offset
            ro_y = offset + idx
            ru_x = width - offset - idx
            ru_y = height - offset
            lu_x = offset
            lu_y = height - offset - idx
            lo = values2dim[lo_y][lo_x]
            ro = values2dim[ro_y][ro_x]
            ru = values2dim[ru_y][ru_x]
            lu = values2dim[lu_y][lu_x]
            # copy over
            values2dim[ro_y][ro_x] = lo
            values2dim[ru_y][ru_x] = ro
            values2dim[lu_y][lu_x] = ru
            values2dim[lo_y][lo_x] = lu
        offset += 1
    print_array(values)    

# print_array(values)
rotate_inplace(values)
