"""Q1:Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a
single line."""
def q1():
    return [str(number) for number in range(2000, 3201) 
            if number % 7 == 0 and number % 5 != 0]
#print(",".join(q1()))

"""Q2:Write a program which can compute the factorial of a given numbers.
Suppose the following input is supplied to the program:
8 Then, the output should be: 40320"""
  
def factorial(n):
    if n == 0: 
       return 1
    else:
       return n * factorial(n - 1)
# num = int(input("Please enter number:"))
# print(factorial(num))

"""Q3.With a given integral number n, write a program to generate a dictionary
that contains (i, i*i) such that is an integral number between 1 and n
(both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8 Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

# def q3(num):
#     return {num: pow(num,2) for num in range(1,num+1)}
# print(q3(8))

"""Q4.Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""

def q4():
    num_str = input("Please enter numbers with comma: ")
    #split comes list
    num_arr = num_str.split(",") 
    num_tuple= tuple(num_arr)
    print(num_arr)
    print(num_tuple)
# q4()

"""Q5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""
class Q5():
    def __init__(self):
        self.str =""
        
    def getString(self):
        self.str = input("Please enter strings:")
    
    def printString(self):
        print(self.str)
    
    def testQ5(self):
        self.getString()
        assert len(self.str) > 100
        self.printString()        
        
# q = Q5()
# q.testQ5()        

"""Q6.Write a program that calculates and prints the value according to the
given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to
the program:
100,150,180
The output of the program should be:
18,22,24"""
import math

def q6():
    C = 50
    H = 30
    values_str = input("Please Enter value with comma: ")
    value = values_str.split(",")
    return [str(int(math.sqrt(2 * C * int(d)/H))) for d in value]

# print(",".join(q6()))

"""Q7.Write a program which takes 2 digits, X,Y as input and generates a 2-
dimensional array. The element value in the i-th row and j-th column of
the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡-Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Array = [ [0] * c for i in range(r) ]"""
def q7():
    num_str = input("Please enter numbers (C,R): ").split(",")
    return [ [0] * int(num_str[1]) for i in range(int(num_str[0]))]
# print(q7())

"""Q8.Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""
def q8():
    str = input("Please enter input: ").lower().split(",")
    print(",".join(sorted(str)))
# q8()

"""Q9.Write a program that accepts sequence of lines as input and prints the
lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""
def q9():
    print("Enter/Paste your content. Ctrl-Z + Enter to save it.")
    lines = []
    while True:
        try:
            line = input().upper()
        except EOFError:
            break
        lines.append(line)
    
    for line in lines:
        print(line)

# q9()
"""Q10.Write a program that accepts a sequence of whitespace separated words as
input and prints the words after removing all duplicate words and sorting
them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""
def q10():
    words = input("Please enter sentences:").split(" ")
    word_list = sorted(list(set(words)))
    print(" ".join(word_list))

q10()
