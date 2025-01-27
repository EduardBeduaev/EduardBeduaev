a = open("24_16388.txt").readline()
c = 0
k = 0
mx = 0
for i in a:
    if (i == "K" and k % 4 == 0) or (i == "L" and k % 4 == 1) or (i == "M" and k % 4 == 2) or (i == "N" and k % 4 == 3):
        c += 1
        k += 1
    elif i == "K":
        mx = max(mx, c)
        k = 1
        c = 1
    elif i == "L":
        mx = max(mx, c)
        k = 2
        c = 1
    elif i == "M":
        mx = max(mx, c)
        k = 3
        c = 1
    elif i == "N":
        mx = max(mx, c)
        k = 4
        c = 1
print(max(mx, c))


