a = open("24_414.txt").readline()
a = a.replace("RUSTEM", " ")
a = a.replace("RUS", "*")

a = a.replace("S", " ")
a = a.replace("U", " ")
a = a.replace("R", " ")
a = a.replace("T", " ")
a = a.replace("E", " ")
a = a.replace("M", " ")

a = a.split()
print(len(a))
