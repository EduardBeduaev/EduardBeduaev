a = open("17_19249.txt")
b = [int(x) for x in a]
kv = [x ** 2 for x in b]
g = max([x for x in b if len(str(abs(x))) == 5 and str(x)[-2:] == "43"])
c = 0
mn = 1000000000000000
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    ks = sorted(k)
    kp = [x for x in ks if len(str(abs(x))) == 5 and str(x)[-2:] == "43"]
    kps = sorted(kp)
    if len(kps) >= 1:
        if k[0] ** 2 + k[1] ** 2 + k[2] ** 2 <= g ** 2:
            mn = min(mn, k[0] ** 2 + k[1] ** 2 + k[2] ** 2)
            c += 1
print(c, mn)
