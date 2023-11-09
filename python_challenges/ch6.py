import numpy as np
from enum import Enum, auto
from array_utils import get_dimension, swap, print_array, get_at 

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

"""Q.5.4a.In the introductory section, I showed how to rotate arrays. 
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
            lo = values2dim[lo_y][lo_x] #top left
            ro = values2dim[ro_y][ro_x] #top right
            ru = values2dim[ru_y][ru_x] #buttom left
            lu = values2dim[lu_y][lu_x] #buttom right
            # copy over
            values2dim[ro_y][ro_x] = lo
            values2dim[ru_y][ru_x] = ro
            values2dim[lu_y][lu_x] = ru
            values2dim[lo_y][lo_x] = lu
        offset += 1
    print_array(values)    
# rotate_inplace(values)

"""Q.5.4b.Write recursive function rotate_inplace_recursive(values2dim) that 
implements the desired 90-degree clockwise rotation."""
def rotate_inplace_recursive(values2dim):
    _ , max_x = get_dimension(values2dim)
    rotate_inplace_recursive_helper(values2dim, 0, max_x - 1)


def rotate_inplace_recursive_helper(values2dim, left, right):
    if left >= right:
        return
    current_width = right - left
    for i in range(current_width):
        lo = values2dim[left + i][left]
        ro = values2dim[right][left + i]
        ru = values2dim[right - i][right]
        lu = values2dim[left][right - i]
        values2dim[left + i][left] = ro
        values2dim[right][left + i] = ru
        values2dim[right - i][right] = lu
        values2dim[left][right - i] = lo
        rotate_inplace_recursive_helper(values2dim, left + 1, right - 1)
    print_array(values) 
    
"""Q.5.5.Initialize a two-dimensional rectangular array with random-based numbers representing 
various types of diamonds or jewels as numerical values. 
The constraint is that initially there must not be three diamonds of the same type placed horizontally 
or vertically in direct sequence. Write function init_jewels_board(width, height, num_of_colors) to 
generate a valid array of the given size and quantity of different types of diamonds.
2 3 3 4 4 3 2
1 3 3 1 3 4 4
4 1 4 3 3 1 3
2 2 1 1 2 3 2
3 2 4 4 3 3 4"""
import random   
def init_jewels_board(width, height, num_of_colors):
    board = []
    for y in range(height):
        board.append([])
        for x in range(width):
            board[y].append(0)

    for y in range(height):
        for x in range(width):
            board[y][x] = select_valid_jewel(board, x, y, num_of_colors)

    return board

def select_valid_jewel(board, x, y, num_of_colors):
    next_jewel_nr = -1
    is_valid = False

    while not is_valid:
        next_jewel_nr = random.randint(1, num_of_colors)

        is_valid = not check_horizontally(board, x, y, next_jewel_nr) and \
                   not check_vertically(board, x, y, next_jewel_nr) and \
                   not check_diagonally(board, x, y, next_jewel_nr)

    return next_jewel_nr
def check_vertically(board, x, y, jewel_nr):
    left1 = get_at(board, x - 1, y)
    left2 = get_at(board, x - 2, y)

    return left1 == jewel_nr and left2 == jewel_nr


def check_horizontally(board, x, y, jewel_nr):
    top1 = get_at(board, x, y - 1)
    top2 = get_at(board, x, y - 2)

    return top1 == jewel_nr and top2 == jewel_nr


# Bonus
def check_diagonally(board, x, y, jewel_nr):
    up_left1 = get_at(board, x - 1, y - 1)
    up_left2 = get_at(board, x - 2, y - 2)

    up_right1 = get_at(board, x + 1, y - 1)
    up_right2 = get_at(board, x + 2, y - 2)

    return up_left1 == jewel_nr and up_left2 == jewel_nr or \
            up_right1 == jewel_nr and up_right2 == jewel_nr
# init_jewels_board(7,5,4)    
        
"""Q.6.2.6.a Write function erase_chains(values2dim) that erases all rows of three or more contiguous diamonds in horizontal
# , vertical, and diagonal orientations from a rectangular playfield array."""  
# jewel = [
#     [1,1,1,2,4,4,3],
#     [1,2,3,4,2,4,3],
#     [2,3,3,1,2,2,3]]

jewel = [
    [1,1,1,2,4,4,3],
    [1,2,3,4,2,4,3],
    [2,3,4,1,2,2,3]]

def erase_chains(values2dim):
    col = len(values2dim[0])
    row = len(values2dim)
    # for row in range(row):
    #     for col in range(col):
    #         checkRight(values2dim, row, col, values2dim[row][col])
    #         checkBottom(values2dim, row, col, values2dim[row][col])
    checkDiagonalForword(values2dim)
    print_array(values2dim)
            
def checkRight(list,row, col, number):    
    col = len(list[0])
    row = len(list)
    for row in range(row):
        for col in range(col):
            if col < len(list[0]) - 3:
                if list[row][col] == list[row][col+1] == list[row][col+2] == number:
                    list[row][col]="-"
                    list[row][col+1]="-"
                    list[row][col+2]="-" 
                    
def checkBottom(list, row, col, number):
    len_col = len(list[0])
    len_row = len(list)
    for row in range(len_row):
        for col in range(len_col):
            if row+2 < len_row:
                if list[row][col] == list[row+1][col] == list[row+2][col] == number and number!="-":
                    list[row][col]="-"
                    list[row+1][col]="-"
                    list[row+2][col]="-"
        if row + 3 != len(list):
            break     
    
def checkDiagonalForword(list):
    len_col = len(list[0])
    len_row = len(list)
    for row in range(len_row):
        for col in range(len_col-1,len_col-5,-1):
            if list[row][col] == list[row+1][col-1] == list[row+2][col-2] and list[row][col]!="-":
                list[row][col]="-"
                list[row+1][col-1]="-"
                list[row+2][col-2]="-"
        if row + 3 != len(list):
            break   
            
erase_chains(jewel)