import functools
def factorial(n):
    return functools.reduce(lambda n_1, n: n_1 * n, range(1, n + 1))