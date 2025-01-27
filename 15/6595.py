def DEL(n, m):
    return n % m == 0


for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = (DEL(x, 3) <= (not (DEL(x, 2))) or (x - a >= 4))
        if not f:
            flag = False
            break
    if flag:
        print(a)
