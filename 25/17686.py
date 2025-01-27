def f(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


for a in range(700_000, 1000_000):
    divs = f(a)
    if not divs:
        continue
    elif str(divs)[-1] == "7" and divs != a and divs != 7:
        print(a, divs)
