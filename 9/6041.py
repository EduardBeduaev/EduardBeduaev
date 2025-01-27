a = open("6041.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    razl = [x for x in bs if bs.count(x) == 1]
    if len(razl) == 3:
        if bs[-1] < bs[0] + bs[1]:
            c += 1
print(c)