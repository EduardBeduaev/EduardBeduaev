a = open("17_6024.txt")
b = [int(x) for x in a]
mxe = max([x for x in b if str(x)[-2:] == "12"])
c = 0
mxs = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    kp = [x for x in k if str(x)[-2:] == "12"]
    if len(kp) == 1:
        if (k[0] + k[1]) ** 2 < mxe ** 2:
            c += 1
            mxs = max(mxs, k[0] + k[1])

print(c, mxs)


