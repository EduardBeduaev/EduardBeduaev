a = open("9156.txt")

for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    pari = [x for x in bs]
    pari2 = [x for x in bs]
    if (bs[0] + bs[-1]) % 3 == 0:

