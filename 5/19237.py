
d = []
def tri(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(1,1000):
    tr = tri(n)
    if n % 3 == 0:
        tr += tr[-2:]
    else:
        tr = tr + tri(tr.count("1"))
    r = int(tr, 3)
    if r % 2 == 0 and r > 220:
        d.append(r)
print(min(d))