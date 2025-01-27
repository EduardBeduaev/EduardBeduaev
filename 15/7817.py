def DEL(m, n):
    return n % m == 0


for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for b in range(40, 61):
            f = (DEL(x, 13) <= (not (x == b))) or (a < x + 20)
            if not f:
                flag = False
                break
    if flag:
        print(a)
