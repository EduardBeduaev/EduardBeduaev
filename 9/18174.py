a = open("18174.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    b_p = [x for x in b if b.count(x) == 2]
    b_s = [x for x in b if b.count(x) == 1]
    b_o = [x for x in b if x < 0]
    b_pol = [x for x in b if x > 0]
    if len(b_p) == 2 and len(b_s) == 4:
        if abs(sum(b_o)) > abs(sum(b_pol)):
            c += 1
print(c)
