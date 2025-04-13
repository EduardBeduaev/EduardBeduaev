a = open("2037.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    proverka = [x for x in b if x > 90]
    summa = sum([x for x in b])
    if len(proverka) == 1 and summa == 180:
        c += 1
print(c)