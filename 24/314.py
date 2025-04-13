a = open("24_314.txt").readline()
a = a.replace("STOCK", " ")
a = a.replace("OCK", "1")
a = a.replace("O", " ")
a = a.replace("C", " ")
a = a.replace("S", " ")
a = a.replace("T", " ")
a = a.replace("K", " ")
c = 0
for i in list(a):
    if i == "1":
        c += 1
print(c)
