def func(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 17 * 16 ** 455 + 2 ** 67 - 4 ** 47 + 58
b = func(a, 8)
c = 0
for i in b:
    if i == 6:
        c += 0
    elif i % 2 == 0:
        c += 1

print(c)
