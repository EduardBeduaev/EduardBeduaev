a = open("12918.txt")

for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    bd = [x for x in bs if bs.count(x) == 2]
    br = [x for x in bs if bs.count(x) == 1]
    if len(bd) == 4 and len(br) == 2:
        if max(bs) not in bd:
            if bs[-1] * bs[0] > (bs[1] + bs[2] + bs[3] + bs[4]):
                print(sum(bs))
                break
