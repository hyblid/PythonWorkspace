import string

def join_numbers(nums):
    return ",".join(str(num) for num in nums)
    
def join_under_10(numbers):
    return ','.join(str(number)
                    for number in numbers
                    if 0 <= number <= 10)

hex_str = ["68", "65", "6C", "6C", "6F"]
def sum_hexes(hex_numbers):
    return sum(int(one_number, 16)
               for one_number in hex_numbers)
    
def reverse_word(filename):
    return [",".join(reversed(lines.split())) 
            for lines in open(filename).readlines()]
    

print(reverse_word("test_file.txt"))
