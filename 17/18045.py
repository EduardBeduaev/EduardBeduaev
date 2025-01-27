a = open("17_18045.txt")
b = [int(x) for x in a]
k = 0
for x in b:
    if 9 < x < 100:
        k += 1

c = 0
ms = 100000000

for i in range(len(b) - 1):
    d = [b[i], b[i + 1]]
    if d[0] % 10 + d[1] % 10 == k:
        c += 1
        ms = min(ms, d[0] + d[1])
print(c, ms)
