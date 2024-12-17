for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (x ** 2 + y ** 2 > 1024 - x) or (y < -2 * x + a)
            if not f:
                flag = False
                break
    if flag:
        print(a)
        break