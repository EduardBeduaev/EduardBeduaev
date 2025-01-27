def f(x):
    s = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return list(s)


for b in range(178_965, 178_982 + 1):
    divs = f(b)
    if len(divs) == 4:
        print(b, divs)
