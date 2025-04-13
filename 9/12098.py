a = open("12098.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    povt = [x for x in b if b.count(x) == 3]
    np = [x for x in b if b.count(x) == 1]
    if len(povt) == 3 and povt[0] % 2 != 0:
        if len(np) == 1 and np[0] % 2 == 0:
            c += 1

print(c)