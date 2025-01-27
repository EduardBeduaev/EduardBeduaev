for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (7 * y + x < a) or (x * x + 3 * y > 98)
            if not f:
                flag = False
                break
    if flag:
        print(a)