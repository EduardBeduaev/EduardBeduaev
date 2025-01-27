def f(x):
    s = ""
    while x > 0:
        s += str(x % 3)
        x = x // 3
    return s[::-1]


d = []
for n in range(1, 1000):
    t = f(n)
    if n % 7 == 0:
        t += t[-3:]
    else:
        t += f(n % 7 * 3)
    r = int(t, 3)
    if r > 369:
        d.append(r)
print(min(d))
