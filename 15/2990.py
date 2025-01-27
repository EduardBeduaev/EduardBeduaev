for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (x * y < 2 * a) or (x >= 11) or (x < 2 * y)
            if not f:
                flag = False
                break
    if flag:
        print(a)