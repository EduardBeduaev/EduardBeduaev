a = open("6925.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    bp = [x for x in b if b.count(x) == 2]
    brazl = [x for x in b if b.count(x) == 1]
    chetn = [x for x in b if x % 2 == 0]
    nechetn = [x for x in b if x % 2 != 0]
    srchent = sum(chetn) / len(chetn) if len(chetn) != 0 else 0
    srnechetn = sum(nechetn) / len(nechetn) if len(nechetn) != 0 else 0
    flag1 = False
    flag2 = False
    if len(bp) == 2 and len(brazl) == 4:
        flag1 = True
    if abs(srchent - srnechetn) > 50:
        flag2 = True
    if (flag1 or flag2) and not(flag1 and flag2):
        c += 1
print(c)
