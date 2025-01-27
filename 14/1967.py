def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 3 * 4**38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1
print(f(a, 16))