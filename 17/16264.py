a = open("17_16264.txt")
b = [int(x) for x in a]
mne = min([x for x in b if 9 < x < 100 and x % (x % 10 + x // 10)])
c = 0
m = 0
for i in range(len(b) - 2):
    k = [b[i], b[i + 1]]
    kratn = [x for x in k if x % mne == 0]
    if k[0] % mne == 0 or k[1] % mne == 0:
        c += 1
        m = max(m, k[0] + k[1])
print(c, m)
