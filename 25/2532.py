def f(x):
    s = set()
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return list(s)



for n in range(137982, 138310 + 1):
    if len(sorted(f(n))) == 2:
        print(n, max(f(n)))
