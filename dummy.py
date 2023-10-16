def decorator(func):
    def wrapper(*args, **kwagrs):
        print("decoration begin")
        func(*args, **kwagrs)
        print("decoration end")
    return wrapper

# @decortor
def func(func_parameter):
    print(func_parameter)

func = decorator(func)
func("something")

"""Decorator with parameters"""
def repetition_decorator(repetitions):
    def decorator(func):
        def wrapper():
            for r in range(repetitions):
                func()
        return wrapper
    return decorator

# @repetition_decorator(5)
def func():
    print("Function")
func = repetition_decorator(4)(func)
func()
