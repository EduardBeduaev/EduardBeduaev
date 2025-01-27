a = open("8946.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    if bs[-1] ** 2 > bs[0] * bs[1] * bs[2] * bs[3]:
        if (bs[-2] + bs[-1]) // 2 > (bs[0] + bs[1] + bs[2]):
            c += 1
print(c)
