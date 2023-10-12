def add_num(num1:int =10, num2:int=20) -> int:
    """this is a test method"""
    print(num1)
    print(num2)
    return num1 + num2

print(add_num.__doc__)
# help(add_num)