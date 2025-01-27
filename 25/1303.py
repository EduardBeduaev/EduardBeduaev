def f(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


for b in range(452_021, 500_000):
    m = sorted(f(b))
    if not m:
        continue
    if m:
        m = min(f(b)) + max(f(b))
        if m % 7 == 3:
            print(b,m)
