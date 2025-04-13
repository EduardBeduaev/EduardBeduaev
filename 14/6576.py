def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


c = 0
b1 = 0
a = 283 ** 382 + 9 ** 15 + 2 ** 3
b = f(a, 14)

for i in b:
    if i == 11:
        c += 1
    elif i == 12:
        b1 += 1

print(abs(c - b1))
