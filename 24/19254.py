a = open("24_19254.txt").readline()
s = ""
d = []
for end in range(len(a)):
    s += a[end]
    if s.count("FSRQ") == 81:
        d.append(len(s) - 1)
        s = s[s.index("FSRQ") + 1:]
print(max(d))






