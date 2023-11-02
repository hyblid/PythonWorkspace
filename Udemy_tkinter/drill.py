import time
import math

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

start = time.perf_counter()
# math.factorial(1000)
print(factorial(10000))
end = time.perf_counter()
print(end - start)