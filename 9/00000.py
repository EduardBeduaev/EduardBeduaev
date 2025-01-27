a = open("00000.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bpo = [x for x in b if b.count(x) == 3]
    bnp = [x for x in b if b.count(x) == 1]
    if len(bpo) == 3 and len(bnp) == 3:
        if bpo[0] >= sum(bnp) / len(bnp):
            c += 1
print(c)