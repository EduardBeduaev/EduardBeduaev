def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 51 * 7 ** 12 - 7 ** 3 - 22
sss = f(a, 7)
print(sum(sss))