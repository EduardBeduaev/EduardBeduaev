def DEL(n, m):
    return n % m == 0

for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = (DEL(x, 2) <= (not(DEL(x, 3)))) or (x + a >= 100)
        if not f:
            flag = False
            break
    if flag:
        print(a)