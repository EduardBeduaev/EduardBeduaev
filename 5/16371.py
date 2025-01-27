d = []
for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += str(bin(n % 3 * 3)[2:])
    r = int(b, 2)
    if r > 195:
        d.append(r)
print(min(d))