a = open("17_2312.txt")
b = [int(x) for x in a]
maxs = max([x for x in b if x % 2 != 0])
mins = min([x for x in b if x % 2 != 0])
ms = 10000000000000
c = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    if (k[0] + k[1]) % 2 == 0:
        if k[0] + k[1] > maxs + mins:
            c += 1
            ms = min(ms, k[0] + k[1])
print(c, ms)
