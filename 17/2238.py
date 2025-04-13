a = open("17_2238.txt")
b = [int(x) for x in a]
sredn = sum(b) / len(b)
c = 0
mx = 0
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    mensi = [x for x in k if x > sredn]
    if len(mensi) >= 2:
        c += 1
        mx = max(mx, k[0] + k[1] + k[2])
print(c, mx)