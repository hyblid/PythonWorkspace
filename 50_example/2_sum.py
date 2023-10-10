
def sum1(*number):
    sum = 0
    for num in number:
        sum += num
    return sum

def sum2(number, start_value=0):
    return sum( number , start_value)

def sum3(numbers):
    return sum(numbers) / len(numbers)

def sum4(word_list):
    len_list = [len(w) for w in word_list]
    tuple = (max(len_list), min(len_list), sum(len_list)/ len(len_list))
    return tuple

def is_intable(one_item):
    try:
        int(one_item)
        return True
    except ValueError:
        return False

def sum5(items):
    int_list = [int(one_item) for one_item in items if is_intable(one_item)]
    return sum(int_list)

lst = ('1', '2', '3', '4', '5')
print(sum5(lst))
    
