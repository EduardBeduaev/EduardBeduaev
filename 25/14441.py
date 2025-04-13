from fnmatch import fnmatch


def f(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return list(s)


for c in range(2068, 10 ** 9 + 1, 2068):
    divs = f(c)
    if fnmatch(str(c), "193*7?"):
        if divs:
            if sum(divs) % 7 == 0:
                print(c, sum(divs))
