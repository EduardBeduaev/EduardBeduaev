a = open("4635.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    bo = [x for x in b if b.count(x) == 2]
    if len(bo) >= 2:
        if bs[1] < bs[-1] and bs[2] < bs[-1]:
            if (min(bs) ** 2) * 2 > bs[1] * bs[2]:
                c += 1
print(c)