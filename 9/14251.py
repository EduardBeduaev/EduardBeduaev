a = open("14251.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    bo = [x for x in bs if bs.count(x) == 2]
    br = [x for x in bs if bs.count(x) == 1]
    if len(bo) == 4 and len(br) == 3:
        if sum(bo) <= sum(x for x in b if x % 2 != 0):
            print(sum(b))
            break
