def f(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


for b in range(900_000, 110_000_0):
    m = sorted(f(b))
    if not m:
        m = 0
        continue
    if m:
        m = max(m) + min(m)
    if str(m)[-2:] == "46":
        print(b, m)
