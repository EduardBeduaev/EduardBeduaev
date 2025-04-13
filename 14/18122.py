def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


for x in range(5556):
    a = 5 ** 150 + 5 ** 135 - x
    b = f(a, 5)
    if b.count(4) == 134:
        print(x)
