a = open("17_2308.txt")
b = [int(x) for x in a]
mxechetn = max([x for x in b if x % 2 == 0])
mxenechetn = max([x for x in b if x % 2 != 0])
chetn = [x for x in b if x % 2 == 0]
nchetn = [x for x in b if x % 2 != 0]
mchetn = min([x for x in b if x % 2 == 0])
mnchetn = min([x for x in b if x % 2 != 0])
c = 0
k = 0
for i in chetn:
    c += 1
for j in nchetn:
    k += 1
if mxechetn > mxenechetn:
    print(c, mchetn)
else:
    print(k, mnchetn)