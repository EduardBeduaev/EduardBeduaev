a = open("24_12254 (1).txt").readline()
c = 0
k = 0
mx = 0
for i in a:
    if (i == "R" and k % 3 == 0) or (i == "S" and k % 3 == 1) or (i == "Q" and k % 3 == 2):
        c += 1
        k += 1
    elif i == "R":
        mx = max(mx, c)
        k = 1
        c = 1
    elif i == "S":
        mx = max(mx, c)
        k = 2
        c = 1
    elif i == "Q":
        mx = max(mx, c)
        k = 3
        c = 1

print(max(mx, c))