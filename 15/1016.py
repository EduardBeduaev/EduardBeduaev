for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (2 * x + 3 * y != 150) or ((x < a) and (y < a))
            if not f:
                flag = False
                break
    if flag:
        print(a)
