a = open("24_1873.txt").readline()
a = a.replace("PR", " ")
a = a.replace("RP", " ")
a = a.split()
print(len(max(a, key=len)))
