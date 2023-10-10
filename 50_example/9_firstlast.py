def firstlast1(sequence):
    return sequence[:1] + sequence[-1:]
# print(firstlast1("abcd"))

def odd_even_sum(numbers):
    evens = []
    odds = []
    for one_number in numbers:
        if one_number % 2:
            odds.append(one_number)
        else:
            evens.append(one_number)
    return [sum(evens), sum(odds)]

# print(odd_even_sum([1,2,3,4,5,6,7,8,9,10]))

"""plus_minus([10, 20, 30, 40, 50, 60]), you’ll get back the result of
10+20-30+40-50+60, or 50."""
def plus_minus(numbers):
    if not numbers:
        return 0

    total = numbers.pop(0)
    while numbers:
        total += numbers.pop(0)

        if numbers:
            total -= numbers.pop(0)
    return total

"""
multiple "for comprehensive" can combine 
myzip([10,20,30], 'abc')
[(10, 'a'), (20, 'b'), (30, 'c')]
"""
def myzip(*args):
    print(len(args[0]))
    return [tuple(a[i] for a in args) #get sequential iterated item with index
                          for i in range(len(min(args, key=len)))] #get range the shortest lenght
    
print(myzip([10,20,30], 'abc'))