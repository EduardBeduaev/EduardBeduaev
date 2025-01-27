from functools import *


@lru_cache(None)
def f(n):
    if n == 3:
        return g(n) == 1
    if n > 3:
        return 5 * f(n - 1) + 6 * g(n - 1) - 3 * n + 8


@lru_cache(None)
def g(n):
    if n == 3:
        return 1
    if n > 3:
        return 6 * f(n - 1) + 5 * g(n - 1) + 3


print(f(9) + g(9))
