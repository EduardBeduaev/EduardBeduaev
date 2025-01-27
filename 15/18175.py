def DEL(x, y):
    return x % y == 0


for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = (not (DEL(x, 7)) and DEL(x, 13)) <= (x > a - 40)
        if not f:
            flag = False
            break
    if flag:
        print(a)
