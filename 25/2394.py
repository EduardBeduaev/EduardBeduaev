def f(n):
    d = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return d


for b in range(550_000, 700_000):
    pass
