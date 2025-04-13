def DEL(n, m):
    return n % m == 0


for a in range(1, 400):
    flag = True
    for b in range(70, 91):
        for x in range(1, 400):
            f = DEL(x, a) or ((x == b) or (DEL(x, 22)))
            if not f:
                flag = False
                break
    if flag:
        print(a)
