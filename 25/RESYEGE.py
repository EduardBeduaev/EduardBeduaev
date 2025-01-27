def f(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)


for b in range(500_000, 700_000):
    divs = f(b)
    for c in divs:
        if str(c)[-1] == "8":
            print(b, c)

# 500002 178
#
# 500004 18
#
# 500016 48
#
# 500018 58
#
# 500020 4348