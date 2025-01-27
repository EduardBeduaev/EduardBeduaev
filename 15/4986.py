def DEL(n, m):
    return n % m == 0

for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for b in range(50,71):
            f = DEL(x, a) or (DEL(x, 23) <= (not(x == b)))
            if not f:
                flag = False
                break
    if flag:
        print(a)