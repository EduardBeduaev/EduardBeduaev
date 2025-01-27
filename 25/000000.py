from fnmatch import fnmatch


def f(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


c = [2 ** n for n in range(1, 1000)]
for b in range(2031, 10 ** 9, 2031):
    if b % 31 == 0:
        if fnmatch(str(b), "*31*65?"):
            if len(f(b)) in c:
                print(b, b // 2031)
