from fnmatch import fnmatch

def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return list(d)


for b in range(4, 100_000_0):
    c = []
    divs = f(b)
    for i in divs:
        if fnmatch(str(i), "4*"):
            c.append(i)
    if len(c) == 24:
        print(b, max(c))
