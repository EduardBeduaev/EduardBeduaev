a = open("4637.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bs = sorted(b)
    if bs[0] > 10 and bs[1] > 10 and bs[2] > 10 and bs[3] > 10:
        if bs[-1] ** 3 <= (bs[0] * bs[1] * bs[2]) ** 2:
            c += 1
print(23 + 11 + 75 + 32)
