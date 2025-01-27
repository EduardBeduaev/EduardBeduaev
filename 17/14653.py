a = open("17.16_14653.txt")
b = [int(x) for x in a]
minpp = sorted([x for x in b if x > 0 and x % 17 == 0])
maxelp = max([x for x in b if str(x)[-2:] == "69"])
c = 0
mks = 1000000000000
for i in range(len(b) - 3):
    k = [b[i], b[i + 1], b[i + 2], b[i + 3]]
    trehz = [x for x in k if len(str(abs(x))) == 3]
    delits = [x for x in k if x % 18 == 0]
    if len(trehz) == 2 and len(delits) == 1:
        if (k[0] + k[1] + k[2] + k[3]) % (minpp[0] + minpp[1]) == 0:
            if k[0] * k[1] * k[2] * k[3] <= maxelp ** 2:
                c += 1
                mks = min(mks, (k[0] + k[1] + k[2] + k[3]) ** 2)
print(c, mks)

