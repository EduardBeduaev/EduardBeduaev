a = open("12241.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bp = [x for x in b if b.count(x) == 2]
    bnp = [x for x in b if b.count(x) == 1]
    if len(bp) == 6 and len(bnp) == 1:
        if (min(bp) + max(bp)) / 2 < sum(bnp):
            c += 1
print(c)
