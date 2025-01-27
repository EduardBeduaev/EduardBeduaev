a = open("24_17535.txt").readline()
s = ""
d = []
for end in range(len(a)):
    s += a[end]
    if s.count("CD") == 161:
        d.append(len(s) - 1)
        s = s[s.index("CD") + 1:]
print(max(d))
