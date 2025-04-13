a = open("17_18582.txt")
b = [int(x) for x in a]
mnel = min([x for x in b])
mx = 0
c = 0
for i in range(len(b) -2):
    k = [b[i], b[i + 1], b[i + 2]]
    otr = [x for x in k if x < 0]
    pol = [x for x in k if x > 0]
    if len(otr) > len(pol):
        if str(k[0] + k[1] + k[2])[-1] == str(mnel)[-1]:
            c += 1
            mx = max(mx, abs(k[0] + k[1] + k[2]))
print(c, mx)