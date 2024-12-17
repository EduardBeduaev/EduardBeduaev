a = open("17_10100.txt")
b = [int(x) for x in a]
g = [x for x in b if str(x)[-1] == "3" and str(x)[-2] == "1"]
d = []
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    c = [x for x in k if len(str(x)) == 3]
    if len(c) == 2:
        if max(g) >= sum(k):
            d.append(sum(k))
print(len(d), max(d))



