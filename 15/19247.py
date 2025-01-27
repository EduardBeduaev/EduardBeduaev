for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (x - 3 * y < a) or (y > 400) or (x > 56)
            if not f:
                flag = False
                break
    if flag:
        print(a)
        break
