"""Q11.Write a program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible by
5 or not. The numbers that are divisible by 5 are to be printed in a
comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010"""
def q11():
    binaries = input("Enter numbers:").split(",")
    b = [b for b in binaries if int(b,2) % 5 == 0]
    print(b)
# 

"""Q12.Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a
single line. hint)[int(d) for d in str(n)]"""
def q12():
    values = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
           values.append(s)
    print (",".join(values))
# print(q12())

"""Q13.Write a program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10 DIGITS 3"""
def q13():
    str = "hello world! 123"
    letter = 0
    digit = 0
    for ch in str:
         if ch.isalpha():
             letter += 1
         if ch.isdigit():
             digit +=1
    # print(f"LETTER {letter}\nDIGIT {digit}")
# q13()
"""Q14.Write a program that accepts a sentence and calculate the number of upper
case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1 LOWER CASE 9"""
def q14():
    str = "Hello World!"
    count = {"UPPER":0, "LOWER":0}
    for ch in str:
         if ch.isupper():
             count["UPPER"] += 1
         if ch.islower():
             count["LOWER"] += 1
    print(f"UPPER {count['UPPER']}\nLOWER {count['LOWER']}")
# q14()
"""Q15.Write a program that computes the value of a+aa+aaa+aaaa with a given
digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106""" 
def q15():
    str = "9"
    pattern_replaced = eval("a+aa+aaa+aaaa".replace("a",str))
    print(pattern_replaced)
# q15()

"""Q16.Use a list comprehension to square each odd number in a list. The list is
input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9"""
def q16():
    return [number for number in range(1,10) if number % 2 == 1]
# print(q16())

"""Q17.Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown
as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""
def q17():
    balance =0
    while True:
        try:
            tranx = input().split(" ")
            if "D" in tranx:
                balance += int(tranx[1])
            elif "W" in tranx:
                balance -= int(tranx[1])
        except EOFError:
            break
    print(f"balnce:{balance}")
# q17()

"""Q18.A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and
will check them according to the above criteria. Passwords that match the
criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""
import re
def q18():
    user_input= "ABd1234@1,a F1#,2w3E*,2We3345"
    value = []
    items=[x for x in user_input.split(',')]
    for p in items:
        if len(p)<6 or len(p)>12:
            continue
        else:
            pass
        
        if not re.search("[a-z]",p):
            continue
        elif not re.search("[0-9]",p):
            continue
        elif not re.search("[A-Z]",p):
            continue
        elif not re.search("[$#@]",p):
            continue
        elif re.search("\s",p):
            continue
        else:
            pass
        value.append(p)
    print (value)
# print(q18())

"""You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are
numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
('Json', '21', '85'), ('Tom', '19', '80')]"""
import operator
def q19():
    person=[]
    while True:
        try:
            information = input("Enter>").split(",")
        except EOFError:
            break
        person.append((information[0],information[1],information[2]))
    sorted_person = sorted(person, key=operator.itemgetter(0,1,2))
    return sorted_person
# print(q19())

"""Q20.Define a class with a generator which can iterate the numbers, which are
divisible by 7, between a given range 0 and n."""
class Gen_number:
    def __init__(self, num):
        self.end = num
    def generate(self):
        return [num for num in range(0, self.end) if num % 7 == 0]
    
g = Gen_number(100)
print(g.generate())    