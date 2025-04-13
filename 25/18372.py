def f(n):
    d = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


for b in range(770000, 0, -1):
    h = f(b)
    if not h:
        continue
    a = sum(h) // len(h)
    if str(a)[-2:] == "12":
        print(b,a)
