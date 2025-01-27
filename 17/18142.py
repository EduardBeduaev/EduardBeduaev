a = open("17_18142.txt")
b = [int(x) for x in a]
mine = min([x for x in b if str(x)[-1] == "8"])
mxs = 0
c = 0

for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    if k[0] % 16 == mine or k[1] % 16 == mine:
        mxs = max(mxs, k[0] + k[1])
        c += 1
print(c, mxs)



