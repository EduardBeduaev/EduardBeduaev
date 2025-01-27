a = open("17_17680.txt")
b = [int(x) for x in a]
minpos = min([x for x in b if x % 41 == 0 and x > 0])
mx = 0
c = 0

for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    if k[0] != k[1]:
        mna = k[0] - k[1]
        if abs(mna) % minpos == 0:
            mx = max(mx, k[0] + k[1])
            c += 1
print(c, mx)
