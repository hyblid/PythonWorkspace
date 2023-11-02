"""Q.5.2.1.Find the common elements of two lists, A and B, and return them as a set.
Implement this, both with and without using matching functions from Python’s sets. 
Write your own function find_common(values1, values2), which works like the Python function intersection()."""
inputA=[1,2,3,7,8]
inputB=[2,3,7,9]
def find_common_without(values1, values2):
    result = set()
    for a in inputA:
        if a in inputB:
            result.add(a)
    return result

def find_common_with(values1, values2):
    return set(values1) & set(values2)
# print(find_common_with(inputA, inputB))

"""Q.5.2.2.Define the basic requirements for a stack and implement class 
Stack based on these requirements using a list."""
class StackIsEmptyException(Exception):
    pass
    
class Stack:
    def __init__(self):
        print("create stack")
        self.data = []    
    #empty()
    def is_empty(self):
        return len(self.data) == 0
    #size()
    def size(self):
        return len(self.data)
    #peek()
    def peek(self):
        if self.is_empty():
            raise StackIsEmptyException()        
        return self.data[-1]
    #push()
    def push(self, value):
        return self.data.append(value)
    #pop()
    def pop(self):        
        if self.is_empty():
            raise StackIsEmptyException() 
        return self.data.pop()
    #get_at()
    def get_at(self, pos):
        return self._values[pos]
    #str
    def __str__(self):
        return "[" + ",".join(self.data) + "]"
    
# s = Stack()
# s.push("one")
# s.push("two")
# print(s)
"""Q.5.2.3a.Write function reverse(values) that returns the elements of the original list 
in reverse order—of course without calling the reverse() function of the list."""

def reverse(values):
    result = []
    for n in values[::-1]:
        result.append(n)
    return result

def reverse_with_comprehension(values):
    return [values[i] for i in range(len(values) - 1, -1, -1)]
# print(reverse(["A", "BB", "CCC", "DDDD"]))
"""Q.5.2.3b.What is different if you want to implement reversing the order inplace 
to be memory- optimal for very large datasets? What should be given then?"""
"lst = [1,2,3,4]"
# def reverse_inplace(orr):
#     index = 0
#     while(index < len(orr)/2):
#         orr[index], orr[(len(orr)-1) - index] = orr[(len(orr)-1) - index], orr[index]
#         index += 1 
        
#     print(orr)
    
def reverse_inplace(original):
    left = 0
    while left < right:
        original[left], original[right] = original[right], original[left]
        left += 1
        right -= 1
    return original
lst = ["1","2","3","4"]
# print(reverse_inplace(lst1))
"""Q.5.2.3.c.Now let’s assume that no performant random index access is available. 
What happens if you want to reverse the order and 
any position-based access will result in O(n) and therefore O(n2) for the complete reversal process. 
How do you avoid this?"""
def list_reverse_with_stack(original):
    s = Stack()
    output = []
    for item in original:
        s.push(item)
    while not s.is_empty():
        output.append(s.pop())
    return output
# print(list_reverse_with_stack(lst))
"""Q.5.2.4.You are supposed to remove duplicate entries from a list. 
The constraint is that the original order should be preserved. Write function remove_duplicates(values)."""
def remove_duplicates(values):
    result = []
    result.append(values[0])
    for num in values[1:-1:1]:
        if num not in result:
            result.append(num)
    print(result)
def remove_duplicates_with_dict(inputs):
    return list(dict.fromkeys(inputs))
lst3 = [1,1,2,3,4,1,2,3]    
# print(remove_duplicates_with_dict(lst3))

"""Q.5.2.5.Imagine that you have a sequence of prices ordered in time 
and that you want to calculate the maximum profit. 
The challenge is to determine at which time (or value, in this case) it would be ideal to buy and to sell. 
Write function max_revenue(prices) for this purpose,
where the temporal order is expressed by the index in the list."""
def max_revenue(prices):
    if not prices:
        return 0  # If there are no prices, the profit is zero.
    min_price = prices[0]  # Initialize the minimum price with the first price.
    max_profit = 0  # Initialize the maximum profit as zero.
    for price in prices:
        if price < min_price:
            min_price = price  # Update the minimum price if a lower price is found.
        else:
            max_profit = max(max_profit, price - min_price)  # Calculate potential profit.
    return max_profit
prices = [250, 270, 230, 240, 222, 260, 294, 210]
# print(max_revenue(prices)) 
"""Q.5.2.6.Suppose you are modeling stock prices or altitudes of a track by a list of numbers. 
Find the longest sequence of numbers whose values ascend or at least stay the same. 
Write function find_longest_growing_sequence(values)."""
def find_longest_growing_sequence(values):
    if not values:
        return []  # If there are no values, return an empty list.
    longest_sequence = [values[0]]  # Initialize the longest sequence with the first value.
    current_sequence = [values[0]]  # Initialize the current sequence with the first value.

    for i in range(1, len(values)):
        if values[i] >= values[i - 1]:
            current_sequence.append(values[i])  # Add the current value to the current sequence.
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence  # Update the longest sequence if needed.
            current_sequence = [values[i]]  # Start a new sequence.

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence  # Check one more time at the end.

    return longest_sequence

# Example usage:
values = [1, 1, 2, 2, 2, 3, 3, 3, 3]
# print(find_longest_growing_sequence(values))
"""Q.5.2.7.Write function check_parentheses(braces_input) 
that checks whether a sequence of braces is neatly nested in each case. 
This should accept any round, square, and curly braces but no other characters."""
def is_matched(expr):
    lefty = "({[" # opening delimiters
    righty = ")}]" # respective closing delims
    s = Stack()
    for c in expr:
        if c in lefty:
            s.push(c) # push left delimiter on stack
        elif c in righty:
            if s.is_empty( ):
                return False # nothing to match with
            if righty.index(c) != lefty.index(s.pop( )):
                return False # mismatched
    return s.is_empty( ) # were all symbols matched?
# print(is_matched("(( ))"))

from enum import Enum, auto
class CheckResult(Enum):
    OK = auto()
    ODD_LENGTH = auto()
    CLOSING_BEFORE_OPENING = auto()
    MISMATCHING_PARENTHESIS = auto()
    INVALID_CHAR = auto()
    REMAINING_OPENING = auto()
    
def is_opening_parenthesis(ch):
    return ch == '(' or ch == '[' or ch == '{'

def is_closing_parenthesis(ch):
    return ch in [")","]","}"]

def is_matching_parenthesis_pair(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '[' and closing == ']') or \
           (opening == '{' and closing == '}')    
def check_parentheses_v2(input):
    # Ungerade Länge kann keine wohlgeformte Klammerung sein
    if len(input) % 2 != 0:
        return CheckResult.ODD_LENGTH
    opening_parentheses = Stack()
    for current_char in input:
        if is_opening_parenthesis(current_char):
            opening_parentheses.push(current_char)
        elif is_closing_parenthesis(current_char):
            if opening_parentheses.is_empty():
                return CheckResult.CLOSING_BEFORE_OPENING
            last_opening_parens = opening_parentheses.pop()
            if not is_matching_parenthesis_pair(last_opening_parens, current_char):
                return CheckResult.MISMATCHING_PARENTHESIS
        else:
            return CheckResult.INVALID_CHAR
    if opening_parentheses.is_empty():
        return CheckResult.OK
    return CheckResult.REMAINING_OPENING
# print(check_parentheses_v2("(( )))"))

"""Q.5.2.8.Write function pascal(n) that computes Pascal’s triangle in terms of nested lists. As you know,
each new line results from the previous one. If there are more than two elements in it, 
two values are added and the sums build the values of the new line. In each case,
a 1 is appended to the front and back.
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]"""
def pascal(n):
    result = []
    pascal_helper(n, result)
    return result

def pascal_helper(n, results):
    if n == 1:
        results.append([1])
    else:
        previous_line = pascal_helper(n - 1, results)
        current_line = calc_line(previous_line)
        results.append(current_line)
    #return increase index
    return results[n - 1]

def calc_line(previous_line):
    current_line = [previous_line[i] + previous_line[i + 1] for i in range(len(previous_line) - 1)]
    return [1] + current_line + [1]
# print(pascal(2))

"""Q.5.2.9.Write function is_magic_triangle(values) that checks whether a sequence of numbers forms a magic triangle. 
Such a triangle is defined as one where the respective sums of the three sides’ values must all be equal."""
def is_magic_triangle_v3(values):
    if len(values) % 3 != 0:
        raise ValueError("Not a triangle: " + len(values))
    side_length = 1 + len(values) // 3
    sum_of_side1 = sum_of_side(values, 0 * (side_length - 1), side_length)
    sum_of_side2 = sum_of_side(values, 1 * (side_length - 1), side_length)
    sum_of_side3 = sum_of_side(values, 2 * (side_length - 1), side_length)
    return sum_of_side1 == sum_of_side2 and sum_of_side2 == sum_of_side3

def sum_of_side(values, start, side_length):
    sum = 0
    for i in range(start, start + side_length):
        sum += values[i % len(values)]
    return sum
# print(is_magic_triangle_v3([1, 5, 3, 4, 2, 6]))
"""q.5.2.10.Write function value_count(values) that determines a histogram (i. e., the distribution of the frequencies of the numbers in the given list).
Also write function sort_dict_by_value(dictionary) to sort the dictionary by its values instead of by keys.
Thereby a descending sorting is to be realized so that smaller values are listed at the beginning.""" 
def value_count(values):
    result = {}
    for v in values:
        if v not in result:
            result[v] = 0
        result[v] += 1
    print(sort_dict_by_value(result))
    

def sort_dict_by_value(dict):
    make_list = list(dict.items())
    length = len(make_list)
    
    for i in range(length-1):
        for j in range(length-i, length):
            if make_list[i][1] > make_list[j][1]:
                temp = make_list[i]
                make_list[i] =make_list[j]
                make_list[j] = temp
    return make_list[-1] 
    
value_count([1, 2, 3, 4, 4, 4, 3, 3, 2, 4])
