a = open("9832.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    bod = [x for x in bs if bs.count(x) == 2]
    vraz = [x for x in bs if bs.count(x) == 1]
    if len(bod) == 4 and len(vraz) == 2:
        if max(vraz) == 1:
            c += 1
print(c)