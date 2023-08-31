import os
from Animal import Animal
os.system("cls")

try:
    num1 = int(input("please input one digit number: "))
    num2 = int(input("please input one digit number: "))

    if num1 >=10 or num2 >=10:
        raise ValueError
    else:
        print("num1: {0} / num2:{1} = {2}".format(num1,num2, num1/num2))
    
except ValueError as err:
    print(err)

else:
    pass

finally:
    pass    
    
    

