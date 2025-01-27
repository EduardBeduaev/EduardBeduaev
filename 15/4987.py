def DEL(n, m):
    return n % m == 0


for a in range(1, 400):
    flag = True
    for b in range(160, 181):
        for x in range(1, 400):
            f = (x == b) <= (DEL(x, 35) <= DEL(x, a))
            if not f:
                flag = False
                break
    if flag:
        print(a)
