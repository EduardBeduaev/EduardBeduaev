from functools import *


def f(n):
    if n < 10:
        return n
    if n >= 10:
        return f(n % 10) + f(n // 10)


@cache
def rec():
    d = []
    for n in range(2 ** 63 - 1):
        if f(n) == 159:
            d.append(n)
    return d


print(len(rec()))
