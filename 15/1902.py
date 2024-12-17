for a in range(1,400):
    flag = True
    for y in range(1, 400):
        for x in range(1, 400):
            f = (y + 2 * x != 48) or (a < x) or (a < y)
            if not f:
                flag = False
                break
    if flag:
        print(a)