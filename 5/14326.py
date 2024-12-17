d = []
for n in range(1, 1000):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "10" + b[2:] + "0"
    else:
        b = "1" + b[:-2] + "10"
    r = int(b, 2)
    if r < 224:
        d.append(n)
print(max(d))
