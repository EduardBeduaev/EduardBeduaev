a = open("10026.txt")
c = 0
g = 0
for i in a:
    c += 1
    b = [int(x) for x in i.split()]
    bp = [x for x in b if b.count(x) > 1]
    bs = sorted(bp)
    if len(bp) > 2 or bs == sorted(bp):
        g += 1
