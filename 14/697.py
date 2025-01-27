def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 9 ** 7 + 3 ** 21 - 8

b = f(a, 3)
print(sum(b))
