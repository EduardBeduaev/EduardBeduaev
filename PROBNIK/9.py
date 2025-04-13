a = open("9.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    brazl = [x for x in b if b.count(x) == 1]
    bodn = [x for x in b if b.count(x) == 2]
    if len(brazl) == 4 and len(bodn) == 2:
        if (sum(brazl) / len(brazl)) > sum(bodn) / len(bodn):
            c += 1
print(c)
#1483