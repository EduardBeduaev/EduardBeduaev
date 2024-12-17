a = open("2_17.txt")
b = [int(x) for x in a]
d = []

for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    mn = min([x for x in k if len(str(x)) == 3])
    if len(k) == 3:
        if mn[-1] == "5":
            if (k[1] + k[2]) % mn == 0:
                d.append(k[1] + k[2])
print(len(d), min(d))
