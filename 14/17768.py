def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 4 ** 644 + 4 **322 + 16 ** 35 - 64 ** 3
c = 0
b = f(a, 4)
for i in b:
    if i == 3:
        c += 1
print(c)