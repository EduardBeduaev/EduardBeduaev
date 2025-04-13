a = open("17_2001.txt")
b = [int(x) for x in a]
c = 0
for i in range(len(b) - 3):
    k = [b[i], b[i + 1], b[i + 2], b[i + 3]]
    chetn = [x for x in k if x % 2 == 0]
    ncht = [x for x in k if x % 2 != 0]
    if (k[0] == chetn and k[1] == ncht) or (k[0] == ncht and k[1] == chetn):
        if (k[2] == chetn and k[3] == ncht) or (k[2] == ncht and k[3] == chetn):
            c += 1
print(c)
