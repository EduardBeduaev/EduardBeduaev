def f(n):
    d = set()
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)

for b in range(1_273_547, 1_400_000):
    divs = f(b)
