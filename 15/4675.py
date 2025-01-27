def DEL(n, m):
    return n % m == 0


for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = (DEL(x, 6) <= (not(DEL(x, 10)))) or (x + a > 121)
        if not f:
            flag = False
            break
    if flag:
        print(a)