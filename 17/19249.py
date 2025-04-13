a = open("17_19249.txt")
b = [int(x) for x in a]
c = 0
mn = 10000000000
maxe = max([abs(x) for x in b if len(str(abs(x))) == 5 and str(abs(x))[-2:] == "43"])

for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    pyat = [x for x in k if len(str(x)) == 5 and str(x)[-2:] == "43"]
    if len(pyat) >= 1:
        if (k[0] ** 2 + k[1] ** 2 + k[-1] ** 2) <= maxe ** 2:
            c += 1
            mn = min(mn, k[0] ** 2 + k[1] ** 2 + k[2] ** 2)

print(c, mn)


