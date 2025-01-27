def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


a = open("17_8954.txt")
b = [int(x) for x in a]
mxe = max([x for x in b if str(f(x, 16))[-3:] == "016"])
mxs = 0
c = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    kratn = [x for x in k if x % 7 == 0]
    if len(kratn) == 1:
        if (k[0] + k[1]) % mxe == 0:
            c += 1
            mxs = max(mxs, k[0] + k[1])
print(c, mxs)
