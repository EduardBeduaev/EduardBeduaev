d = []
for n in range(1, 1000):
    b = bin(n)[2:]
    if len(b) % 2 == 0:
        b += "1"
    else:
        b = "1" + b + "0"
    r = int(b, 2)
    if r > 666:
        d.append(r)
print(min(d))
