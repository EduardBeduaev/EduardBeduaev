a = open("3730.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    if sum(bs) // len(bs) < (bs[1] + bs[2] + bs[3]) // 3:
        c += 1
print(c)