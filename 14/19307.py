def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 15_625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
b = f(a, 5)
print(b)