for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (x >= 9) or (2 * x < y) or (x * y < a)
            if not f:
                flag = False
                break
    if flag:
        print(a)