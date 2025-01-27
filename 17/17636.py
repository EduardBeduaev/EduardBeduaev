a = open("17_17636.txt")
b = [int(x) for x in a]
trz = max([x for x in b if len(str(abs(x))) == 3 and str(x)[-1] == "3"])
c = 0
mxs = 0
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    trz2 = [x for x in k if len(str(abs(x))) == 3 and str(x)[-1] == "3"]
    if k[0] + k[1] + k[2] < trz:
        if len(trz2) >= 1:
            mxs = max(mxs,k[0] + k[1] + k[2])
            c += 1
print(c, mxs)



