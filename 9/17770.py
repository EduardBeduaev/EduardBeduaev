a = open("17770.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    b_u = [x for x in bs if str(x)[-1] == "5"]
    if sum(bs[-2:]) * 2 > sum(bs[:-2]) * 3:
        if len(b_u) >= 2:
            c += 1
print(c)
