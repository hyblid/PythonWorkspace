def foo(x):
    def bar(y):
        return x * y
    return bar

f = foo(10)
print(f(20))