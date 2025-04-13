a = open("24_19254.txt").readline()
c = 0
for i in range(len(a)):
    if a[i] == "Q" and a[i -3:] == "FSR":
        c += 1
    if c == 80:







