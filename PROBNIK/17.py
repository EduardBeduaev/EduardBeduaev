a = open("17 (10).txt")
b = [int(x) for x in a]
me = max([x for x in b if str(x)[-3:] == "538"])
c = 0
mx = 0
for i in range(len(b) - 3):
    k = [b[i], b[i + 1], b[i + 2], b[i + 3]]
    pyat = [x for x in k if len(str(x)) == 5]
    npyat = [x for x in k if len(str(x)) != 5]
    krant3 = [x for x in k if x % 3 == 0]
    kratn7 = [x for x in k if x % 7 == 0]
    if len(pyat) >= 2 and len(npyat) >= 1:
        if len(krant3) > len(kratn7):
            if (k[0] + k[1] + k[2] + k[3]) > me:
                if (k[0] + k[1] + k[2] + k[3]) < me * 2:
                    c += 1
                    mx = max(mx, k[0] + k[1] + k[2] + k[3])
print(c, mx)
#260 106865
