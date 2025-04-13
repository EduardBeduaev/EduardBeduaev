d = []
for n in range(20,601):
    b = bin(n)[2:]
    b = b[:-2]
    r = int(b, 2)
    if r:
        d.append(r)
print(len(d))


