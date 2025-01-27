a = open("17_12926.txt")
b = [int(x) for x in a]
mxs = max([x for x in b if x > 0 and len(str(x)) == 2])
c = 0
mine = 100000000000000000

k = []
for i in range(len(b) - 3):
    if str(b[i])[-1] == str(b[i + 1])[-1] == str(b[i + 2])[-1] == str(b[i + 3])[-1]:
        k.append([b[i], b[i + 1], b[i + 2], b[i + 3]])
A = max([sum(x) for x in k])

for v in range(len(b) - 4):
        k1 = [b[v], b[v + 1], b[v + 2], b[v + 3], b[v + 4]]
        mensjia = [x for x in k1 if x < A]
        if len(mensjia) == 1:
            if sum(k1) % mxs == 0:
                c += 1
                mine = min(mine, sum(k1))

print(c, mine)
