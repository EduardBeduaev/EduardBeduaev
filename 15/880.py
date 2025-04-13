def DEL(n,m):
    return n % m == 0

for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = DEL(70,a) and (not (DEL(x, a))) <= (DEL(x,18) <= (not (DEL(x, 42))))
        if not f:
            flag = False
            break
    if flag:
        print(a)