def firstlast1(sequence):
    return sequence[:1] + sequence[-1:]

def odd_even_sum(numbers):
    evens = []
    odds = []

    for one_number in numbers:
        if one_number % 2:
            odds.append(one_number)
        else:
            evens.append(one_number)

    return [sum(evens), sum(odds)]

def plus_minus(numbers):
    if not numbers:
        return 0

    total = numbers.pop(0)

    while numbers:
        total += numbers.pop(0)

        if numbers:
            total -= numbers.pop(0)

    return total

def myzip(*args):
    print(len(args[0]))
    return [tuple(a[i] for a in args)
            for i in range(len(min(args, key=len)))]
    
print(myzip([10, 20,30], 'abc'))