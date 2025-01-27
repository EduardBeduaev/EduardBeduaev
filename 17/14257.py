a = open("17_14257.txt")
b = [int(x) for x in a]
bpyat = max([x for x in b if len(str(abs(x))) == 5 and str(x)[-1] == "7"])
mn = 100000000
c = 0
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]

    b12 = [x for x in k if str(x)[-2:] == "12"]

    if len(b12) == 2:
        if k[0] + k[1] + k[2] <= bpyat:
            mn = min(mn, k[0] + k[1] + k[2])
            c += 1
print(c, abs(mn))
