a = open("17_17530.txt")
b = [int(x) for x in a]
bm = min([x for x in b])
sm = 1000000
c = 0

for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    ks = sorted(k)
    deli = [x for x in ks if x % 55 == bm]
    if len(deli) >= 1:
        c += 1
        sm = min(sm, k[0] + k[1])
print(c, sm)