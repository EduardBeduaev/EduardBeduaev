d = []
for n in range(1,1000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b.replace("0", "11")
    else:
        b = b.replace("1","10")
    r = int(b, 2)
    if r <= 161:
        d.append(r)
print(max(d))