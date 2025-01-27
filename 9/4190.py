a = open("4190.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    if len(bs) == 5:
        if min(bs) ** 2 + max(b) ** 2 > bs[1] ** 2 + bs[2] ** 2 + bs[3] ** 2:
            c += 1
print(c)
