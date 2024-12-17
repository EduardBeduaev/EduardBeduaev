a = open("17 (8).txt")
b = [int(x) for x in a]
c = 0
d = []
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    pari = [x for x in k if sum(k) % 2 != 0 and (k[0] * k[1]) % 5 == 0]
    mxsum = [x for x in pari if max]
        c += 1
        print(c)