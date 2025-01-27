a = open("17_17873.txt")
b = [int(x) for x in a]
mn = min([x for x in b])
mxs = 0
c = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    if k[0] % 16 == mn or k[1] % 16 == mn:
        mxs = max(mxs, k[0] + k[1])
        c += 1
print(c, mxs)
