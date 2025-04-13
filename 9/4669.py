a = open("4669.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    if (min(bs) + max(bs)) < (bs[1] + bs[2]):
        c += 1
print(c)
