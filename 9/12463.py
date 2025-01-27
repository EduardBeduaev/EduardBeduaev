a = open("12463.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bpovt1 = [x for x in b if b.count(x) == 4]
    bpovt2 = [x for x in b if b.count(x) == 2]
    bnp = [x for x in b if b.count(x) == 1]
    if len(bpovt1) == 4 and len(bpovt2) == 2 and len(bnp) == 3:
        if sum(bnp) // len(bnp) >= max(bpovt1) or max(bpovt2):
            c += 1

print(c)