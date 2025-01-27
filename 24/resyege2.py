a = open("24_demo (3).txt").readline()

a = a.replace("X", " ")
a = a.replace("Z", " ")
a = a.split()
print(len(max(a, key=len)))
