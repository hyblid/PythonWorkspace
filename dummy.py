def foo():
    yield 1
    yield 2
    yield 3


g = foo()
for one_item in g:
    print(one_item)