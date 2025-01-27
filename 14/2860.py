def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


a = 5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 - 98
b = f(a, 7)
print(b)
