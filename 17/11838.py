a = open("17_11838.txt")
b = [int(x) for x in a]
maxs = max([x for x in b if str(x)[-2:] == "50"])
mx = 0
c = 0
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    razl = [x for x in k if k.count(x) == 1 and len(str(x)) == 5]
    if (k[0] + k[1] + k[2]) <= maxs:
        c += 1
        mx = max(mx, k[0] + k[1] + k[2])
print(c,mx)

