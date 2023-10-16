"""Q61.Print a unicode string "hello world"."""
str1 = u"hello world"
# print(str1)

"""Q62.Write a program to read an ASCII string and to convert it to a unicode
string encoded by utf-8."""
str2= "hello world".encode("utf-8")
# print(str2)

"""Q63.Write a special comment to indicate a Python source code file is in
unicode."""
# -*- coding: utf-8 -*-

# """Q64.Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
# console (n>0)."""
# # n = int(input("Please enter n: "))
# # sum = 0
# # for n in range(1,n+1):
# #    sum += (n/(n+1))
# # print(round(sum,2)) 
# """Q65.Write a program to compute:
# f(n)=f(n-1)+100 when n>0 and f(0)=1
# with a given n input by console (n>0)."""
# # def f(n):
# #     if n==0:
# #         return 1
# #     else:
# #         return f(n-1)+100
# # print(f(5))

"""Q66.The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input
by console."""
def f(n):
    if n <= 1: 
        return n
    else:
        return f(n-1)+f(n-2)
# print(fib(9))
"""Q67.The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci
Sequence in comma separated form with a given n input by console."""
# n=int(input("c:>"))
# values = [str(f(x)) for x in range(0, n+1)]
# print(",".join(values))
"""Q68.Please write a program using generator to print the even numbers between
0 and n in comma separated form while n is input by console."""
def even_generator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield str(i)
        i+=1

# values = even_generator(9)
# print(",".join(values))

"""Q69.Please write a program using generator to print the numbers which can be
divisible by 5 and 7 between 0 and n in comma separated form while n is
input by console."""
def num_generator(n):
    i=0
    while i<=n:
        if (i%5==0) and (i%7==0):
            yield str(i)
        i+=1

# values = num_generator(100)
# print(",".join(values))
"""Q70.Please write assert statements to verify that every number in the list
[2,4,6,8] is even."""
lst = [2,4,6,8]
for n in lst:
    assert n%2 ==0    

