def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


c = 0
for x in range(1, 2030):
    g = 7 ** 91 + 7 ** 160 - x
    sem = f(g, 7)
    d = 0
    for b in sem:
        if b == 0:
            c += 1
            d += 1
            if d == 70:
                print(x)
