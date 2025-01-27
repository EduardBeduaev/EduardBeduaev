d = []
for n in range(1, 1000):
    b = bin(n)[2:]
    b += str((b.count("1") % 2))
    b += str((b.count("1") % 2))
    r = int(b, 2)
    if r > 60:
        d.append(r)
print(min(d))