a = open("17_1998.txt")
b = [int(x) for x in a]
c = 0
mx = 0
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    summa = k[0] + k[1] + k[2]
    proizv = k[0] * k[1] * k[2]
    if str(summa)[-1] == "5":
        if proizv % 7 == 0:
            c += 1
            mx = max(mx, k[0] + k[1] + k[2])
print(c, mx)