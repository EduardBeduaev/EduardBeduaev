a = open("17_7819.txt")
b = [int(x) for x in a]
mxdv = max([x for x in b if len(str(x)) == 2])
c = 0
mx = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    check1 = [x for x in k if x > 0 and len(str(x)) == 3]
    if len(check1) >= 1:
        if (k[0] + k[1]) % mxdv == 0:
            c += 1
            mx = max(mx, k[0] + k[1])
print(c, mx)