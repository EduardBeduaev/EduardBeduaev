a = open("15321.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    bp1 = [x for x in bs if bs.count(x) == 2]
    bnp = [x for x in bs if bs.count(x) == 1]
    if len(bp1) == 2 and len(bnp) == 2:
        if bs[-1] < (b[0] + b[1] + b[2]):
            c += 1
print(c)
