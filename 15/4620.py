for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (x + y <= 22) or (y <= x - 6) or (y >= a)
            if not f:
                flag = False
                break
    if flag:
        print(a)