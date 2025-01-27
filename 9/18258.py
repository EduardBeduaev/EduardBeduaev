d = []
a = open("18258.txt")
c = 0
for i in a:
    c += 1
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    bpovt = [sum(map(int,str(x))) for x in bs if bs.count(x) > 1]
    if len(bpovt) > 1:
            d.append(c)
print(max(d))