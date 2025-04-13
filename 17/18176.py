a = open("17_18176.txt")
b = [int(x) for x in a]
mne = min([x for x in b if x > 0 and str(x)[-1] == "4"])
ms = 0
c = 0
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    summa1 = sum(map(int, list(str(abs(k[0])))))
    summa2 = sum(map(int, list(str(abs(k[1])))))
    summa3 = sum(map(int, list(str(abs(k[2])))))
    if summa1 + summa2 + summa3 == mne:
        c += 1
        ms = max(ms, k[0] + k[1] + k[2])
print(c, ms)
