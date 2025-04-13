def f(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return list(s)


for a in range(902_714, 950_000):
    divs = f(a)
    l = []
    poisk = sorted([x for x in divs if x != 5 and str(x)[-1] == "5"])
    if poisk:
        print(a, poisk[0])

