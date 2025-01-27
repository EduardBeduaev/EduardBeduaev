def f(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


for i in range(800_001, 900_000):
    d = []
    for a in f(i):
        if str(a)[-1] == "9" and a != i and a != 9:
            d.append(a)
    if d:
        print(i, min(d))

