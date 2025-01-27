a = open("17_18368.txt")
b = [int(x) for x in a]
mne = min([x for x in b if str(abs(x))[-1] == "7"])
mxp = 0
c = 0
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    pyat = [x for x in k if len(str(abs(x))) == 5]
    if len(pyat) >= 1:
        if (k[0] * k[1] * k[2]) % mne == 0:
            c += 1
            mxp = max(mxp, k[0] * k[1] * k[2])
print(c, mxp)
