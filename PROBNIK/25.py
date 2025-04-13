def f(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return list(s)


for d in range(800_000, 900_000):
    divs = f(d)
    if divs:
        m = min(divs) + max(divs)
        if str(m)[-1] == "4":
            print(d, m)

# #800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554