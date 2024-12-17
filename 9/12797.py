a = open("12797.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bpo = [x for x in b if b.count(x) == 2]
    bnp = [x for x in b if b.count(x) == 1]
    ch = [x for x in bpo if x % 2 == 0]
    nch = [x for x in bnp if x % 2 != 0]
    if len(ch) == 2 and len(nch) == 2:
        c += 1
print(c)