a = open("17_4705.txt")
b = [int(x) for x in a]
mxe = max([x for x in b if str(x)[-1] == "3"])
mx = 0
c = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    odnoc = [x for x in k if str(x)[-1] == "3"]
    if len(odnoc) == 1:
        if k[0] ** 2 + k[1] ** 2 >= mxe ** 2:
            c += 1
            mx = max(mx, k[0] ** 2 + k[1] ** 2)
print(c, mx)
