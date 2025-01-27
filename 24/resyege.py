a = open("24_demo (1).txt").readline()
while "XX" in a or "YY" in a or "ZZ" in a:
    if "XX" in a:
        a = a.replace("XX", "X X")
    if "YY" in a:
        a = a.replace("YY", "Y Y")
    if "ZZ" in a:
        a = a.replace("ZZ", "Z Z")
a = a.split()


print(len(max(a, key=len)))
