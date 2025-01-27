a = open("14249.txt")

for i in a:
    b = [int(x) for x in i.split()]
    chetn = [x for x in b if x % 2 == 0]
    nch = [x for x in b if x % 2 != 0]
    ravns = [sum(map(int,str(x))) for x in b if  ]
    if len(chetn) == len(nch):