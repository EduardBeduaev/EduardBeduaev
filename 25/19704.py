def f(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(n // i)
            s.add(i)
    return list(s)

for c in range(333_555, 777_999 + 1):
    divs = f(c)
    check = [x for x in divs if len(str(x)) == 2]
    if len(check) == 35:
        print(c, min(check), max(check))