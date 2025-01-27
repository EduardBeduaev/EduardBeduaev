def DEL(m, n):
    return n % m == 0


for a in range(1, 400):
    flag = True
    for c in range(30, 46):
        for x in range(1, 400):
            f = (DEL(x, a) and (x == c)) <= (not (DEL(x, 12)))
            if not f:
                flag = False
                break
    if flag:
        print(a)
