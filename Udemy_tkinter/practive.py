def decorator(func):
    def wrapper():
        print("decorator begins")
        func()
        print("decorator ends")
    return wrapper

@decorator
def fun():
    print("Function out side decorator")

# func = decorator(function)
# func()

fun() #With @decorator