a = open("17_10719.txt")
b = [int(x) for x in a]
c = 0
mx = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    zakna13 = [x for x in k if str(abs(x))[-2:] == "13"]
    if len(zakna13) == 1:
        c += 1
        mx = max(mx, k[0] + k[1])
print(c, mx)