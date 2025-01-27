import sys

sys.setrecursionlimit(8000)

def g(n):
    if n > 2:
        return f(n - 1) - g(n - 2)

def f(n):
    if n <= 2:
        return g(n) == n
    if n > 2:
        return g(n) + f(n - 2)


print(f(15))
