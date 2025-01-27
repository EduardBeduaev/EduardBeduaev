c = 0
a = open("19241.txt")
for i in a:
    b = [int(x) for x in i.split()]
    c += 1
    bpovt = [x for x in b if b.count(x) == 3]
    bnp = [x for x in b if b.count(x) == 1]
    if len(bnp) == 1 and len(bpovt) == 6:
        if sum(bpovt) / len(bpovt) < bnp[0]:
            print(c)
