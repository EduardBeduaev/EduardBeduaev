def DEL(x, y):
    return x % y == 0


for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (DEL(x, 15) and (not (DEL(x, 10)))) <= (a < x + 50)
            if not f:
                flag = False
                break
    if flag:
        print(a)
