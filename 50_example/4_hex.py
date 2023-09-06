from decimal import Decimal

def hex_output1():

    hex_str = input('Enter a hex number to convert: ')
    dec_num = sum(int(x, 16) * pow(16, len(hex_str)-i-1) 
                  for i, x in enumerate(hex_str))
    print(dec_num)
    
def hex_output2():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        if 48 <= ord(digit) <= 57:
            dec_digit = ord(digit) - 48
        elif 97 <= ord(digit) <= 102:
            dec_digit = ord(digit) - 87

        decnum += dec_digit * (16 ** power)
    print(decnum)
    
def hex_output3():
    name = input('Enter your name: ')
    for index, char in enumerate(name):
        print(name[:index+1])

    
    
hex_output2()
    
    
    
    
    