d = []
for n in range(1, 1000):
    b = bin(n)[2:]
    s = str(b)
    s += str(b.count("1") % 2)
    s += str(b.count("1") % 2)
    r = int(b, 2)
    if r > 75:
        d.append(r)
print(min(d))
