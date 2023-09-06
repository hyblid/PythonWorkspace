from decimal import Decimal

def run_timing1():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')
        if not one_run:
            break

        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs

    print(f'Average of {average_time}, over {number_of_runs} runs')
    

def run_timing2():
    #1234.5678,2,3
    f = input("please enter float  numbers: ")
    int1 = int(input("please enter int1 numbers: "))
    int2 = int(input("please enter int2 numbers: "))
    index = f.find(".")
    print(index)
    num1 = f[(index - int1):(index + int2)]
    # num2 = f[index: (index + int2)]
    print(num1)
    
def run_timing3():
    f1 = input("please enter float1 numbers: ")
    f2 = input("please enter float2 numbers: ")
    sum = float(Decimal(f1) + Decimal(f2))
    print(f"{f1} + {f2} = {sum}")    
   
    
run_timing3()   
        
