a = open("24_7600.txt").readline()

a = a.replace("Q", "*")
a = a.replace("S", "*")
a = a.replace("R", "*")
while "**" in a:
    a = a.replace("**", "* *")

a = a.split()
print(len(max(a, key=len)))
