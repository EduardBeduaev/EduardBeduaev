a = open("18258.txt")
c = 0
k = 0
for i in a:
    b = [int(x) for x in i.split()]
    k += 1
    bs = sorted(b)
    bpovtor = [x for x in bs if sum(map(int,str(x))) % 2 == 0 and bs.count(x) > 1]
    if len(bpovtor) > 1:
        if b == bs:
            print(k)

