a = open("17_17558.txt")
b = [int(x) for x in a]
bkratn = [x for x in b if x % 32 == 0]
mxs = 0
c = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    bo = [x for x in k if x < 0]
    if len(bo) >= 1:
        if k[0] + k[1] < len(bkratn):
            mxs = max(mxs, k[0] + k[1])
            c += 1
print(c, mxs)
