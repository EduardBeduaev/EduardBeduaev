a = open("16256.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    br = [x for x in b if b.count(x) == 1]
    bo = [x for x in b if b.count(x) == 1]
    if len(br) == 2:
        for a in range(len(bo) - 1):
            k = [b[a], b[a + 1]]
            if k[0] + k[2] < br[0] + b[1] + bo[-1]:
                c += 1

print(c)