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
print(is_matched("(( ))"))
 