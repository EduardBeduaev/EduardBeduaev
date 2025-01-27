def DEL(n,m):
    return n % m == 0

for a in range(1,400):
    flag = True
    for x in range(1, 400):
        f = (DEL(x, a) and DEL(x, 24) and (not DEL(x, 16))) <= (not DEL(x, a))
        if not f:
            flag = False
            break
    if flag:
        print(a)