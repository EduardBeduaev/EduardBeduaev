a = open("24_1040.txt").readline()
a = a.replace("0", "*")
a = a.replace("1", "*")
a = a.replace("2", "*")
a = a.replace("3", "*")
a = a.replace("4", "*")
a = a.replace("5", "*")
a = a.replace("6", "*")
a = a.replace("7", "*")
a = a.replace("8", "*")
a = a.replace("9", "*")

for x in "qwertyuiopasdfghjklzxcvbnm":
    a = a.replace(x, " ")

a = a.split()

print(len(max(a, key=len)))
