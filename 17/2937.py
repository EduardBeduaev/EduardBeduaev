a = open("17_2937.txt")
b = [int(x) for x in a]
mxe = max([x for x in b if abs(x) % 11 == 0])
c = 0
mx = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    kratn = [x for x in k if x % 11 == 0]
    if len(kratn) >= 1:
        if k[0] + k[1] <= mxe:
            c += 1
            mx = max(mx, k[0] + k[1])
print(c, mx)