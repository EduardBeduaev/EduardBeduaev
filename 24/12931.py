a = open("24_12931.txt").readline()
k = 0
c = 0
mx = 0
for i in a:
    if (i == "V" and k % 5 == 0) or (i == "W" and k % 5 == 1) or (i == "X" and k % 5 == 2) or (i == "Y" and k % 5 == 3) or (i == "Z" and k % 5 == 4):
        k += 1
        c = 1
    elif i == "V":
        mx = max(mx, c)
        k = 1
        c = 1
    elif i == "W":
        mx = max(mx, c)
        k = 2
        c = 1
    elif i == "X":
        mx = max(mx, c)
        k = 3
        c = 1
    elif i == "Y":
        mx = max(mx, c)
        k = 4
        c = 1
    elif i == "Z":
        mx = max(mx, c)
        k = 5
        c = 1
print(max(mx, c))