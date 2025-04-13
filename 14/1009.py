def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 7 ** 21 + 49 ** 13 - 7 ** 10
c = 0
for i in f(a, 7):
    if i == 6:
        c += 1
print(c)
print(f(a,7))