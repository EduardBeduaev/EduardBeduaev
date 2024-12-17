a = open("7611.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    br = [x for x in bs if bs.count(x) == 1]
    if len(br) == 5:
        if (br[0] + br[-1]) * 2 < (br[1] + br[2] + br[3]):
            c += 1

print(c)
