a = open("17_16328.txt")
b = [int(x) for x in a]
mne = min([x for x in b if x % 19 == 0])
mx = 0
c = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    odnochisl = [x for x in k if x % mne == 0]
    if len(odnochisl) >= 1:
        c += 1
        mx = max(mx, k[0] + k[1])
print(c, mx)