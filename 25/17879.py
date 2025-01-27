def f(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


for b in range(800_000, 1000_001):
    m = sorted(f(b))
    if not m:
        m = 0
        continue
    if m:
        m = max(f(b)) + min(f(b))
    if str(m)[-1] == "4":
        print(b, m)

