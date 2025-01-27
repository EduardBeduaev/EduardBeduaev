a = open("17_17750.txt")
b = [int(x) for x in a]
mne = min([x for x in b])
c = 0
mxp = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    if k[0] % 77 + k[1] % 77 == mne:
        c += 1
        mxp = max(mxp, k[0] + k[1])
print(c, mxp)

