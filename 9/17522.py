a = open("17522.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    br = [x for x in bs if bs.count(x) == 2]
    if bs[-1] < bs[0] + bs[1] + bs[2] and len(br) == 2:
        c += 1
print(c)
