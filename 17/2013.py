a = open("17_2013.txt")
b = [int(x) for x in a]
# el = [x for x in b if str(x)[-1] == "2" or str(x)[-1] == "7" and x % 3 == 0 and x % 11 == 0]
# print(len(el), min(el))
d = []
for i in b:
    if str(i)[-1] == "2" or str(i)[-1] == "7":
        d.append(i)
dm = []
for el in d:
    if el % 3 == 0 and el % 11 == 0:
        dm.append(el)
print(len(dm), min(dm))