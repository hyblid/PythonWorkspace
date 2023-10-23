import math
"""Q2_1_a Write function calc(m, n) that multiplies two variables m and n of type int, 
then divides the product by two, and outputs the remainder with respect to division by 7."""
def calc(num1, num2):
    result = (num1*num2//2)%7
    print(result)
# q2_1(5,5)
"""Q2_1_b.Count as well as sum up the natural numbers that are divisible by 2 or 7 
up to a given maximum value (exclusive) and output it to the console. 
Write function calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive). 
Extend it so that it returns the two values instead of performing the console output."""
def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    num_set = set()
    for num in range(2,max_exclusive):
        if num % 2 == 0 or num %7 ==0:
            num_set.add(num)
    print(num_set)
    print(f"count:{len(num_set)}, sum:{sum(num_set)}")    
# calc_sum_and_count_all_numbers_div_by_2_or_7(15)

"""Q2_2_1cCreate the functions is_even(n) and is_odd(n) that will check if the passed integer is even or odd, respectively."""
def is_odd(n):
    return n%2==1

def is_even(n):
    return n%2==0

"""Q2_2_2.Write function number_as_text(n) which, 
for a given positive number, converts the respective digits into corresponding text."""
value_to_text_mapping = {
    0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR",
    5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"
}
def number_as_text(n):
    value_to_text = ""
    for ch in str(n):
        remainder = value_to_text_mapping[int(ch) % 10]
        value_to_text += remainder + " "
    return value_to_text
# print(number_as_text(1245))

"""Q2_2_3.By definition, a natural number is called a perfect number if its value is equal to the sum of its real divisors.
This is true, for example, for the numbers 6 and 28"""
def is_perfect_num(value):
    num = []
    for i in range(1, value // 2 + 1):
        if value % i == 0:
            num.append(i)
    return sum(num) == value

def calc_perfect_numbers(max_exclusive):
    return [num for num in range(2, max_exclusive+1) if is_perfect_num(num)]
# print(calc_perfect_numbers(10000))
"""Q2_2_4.Write function calc_primes_up_to(max_value) to compute all prime numbers 
up to a given value. As a reminder, a prime number is a natural number greater than 1 
and exclusively divisible by itself and by 1. To compute a prime number, 
the Sieve of Eratosthenes was described before."""
def is_prime(potentially_prime):
    for i in range(2, potentially_prime // 2 + 1):
        if potentially_prime % i == 0:
            return False
    return True
def calc_primes_up_to(max_value):
    return [num for num in range(2, max_value) if is_prime(num)]

# print(calc_primes_up_to(15))
"""Q2_2_5.Compute all pairs of prime numbers with a distance of 2 (twin), 4 (cousin), and 6 (sexy)
up to an upper bound for n. For twins then the following is true"""
def prime_number_pairs(litmit_num):
    twin={}
    cousin={}
    sexy={}
    for num in range(2, litmit_num):
        if is_prime(num) and is_prime(num+2):
            twin[num] = num+2 
        if is_prime(num) and is_prime(num+4):
            cousin[num] = num+4 
        if is_prime(num) and is_prime(num+6):
            sexy[num] = num+6
    # print("twin", twin)
    # print("cousin",cousin)
    # print("sexy", sexy)

prime_number_pairs(50)
"""Q2_2_7.Create function calc_checksum(digits) that performs the following 
position-based calculation for the checksum of a number of any length given as a string, 
with the n digits modeled as z1 to zn:"""
def calc_checksum(digit):
    user_sum = []
    for index, num in enumerate(digit, 1):
        user_sum.append(index * int(num))
    print(sum(user_sum)%10)
# calc_checksum("11111")
"""Q2_2_7a.Write function from_roman_number(roman_number) 
that computes the corresponding decimal number from a textually valid Roman number
For syntactically invalid Roman numbers, such as IXD, 
an incorrect result, here 489, can be computed by applying subtraction rule twice in a row: 0 − 1 − 10 + 500.
    print(from_roman_number("VII")-7)
    print(from_roman_number("XXII")-42)
    print(from_roman_number("XXIXV")-)"""
value_map = {"I": 1, "V": 5, "X": 10, "L": 50,
             "C": 100, "D": 500, "M": 1000}
int_to_roman_digit_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                          40: "XL", 50: "L", 90: "XC", 100: "C",
                          400: "CD", 500: "D", 900: "CM", 1000: "M"}

def from_roman_number(roman_number):
    value = 0
    last_digit_value = 0
    for roman_digit in reversed(roman_number):
        digit_value = value_map[roman_digit]

        add_mode = digit_value >= last_digit_value
        if add_mode:
            value += digit_value
            last_digit_value = digit_value
        else:
            value -= digit_value
    return value

def to_roman_number(value):
    result = ""
    remainder = value

    # absteigende Skiikortie
    for i in sorted(int_topp_rom
"""::::"""":::::""""
            romaroman_digit_map[
emainder = divmod(remainder, multiplier)
            iiiiresult += roman_digit * timesh
def index_text(str   fojjjjjr num in range(2, -1, -1):
        print(stkr[num])
        iii
print(from_roman_number("VII"))
print(from_roman_.ii