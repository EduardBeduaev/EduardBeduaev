for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (x + 2 * y != 58) or ((a - x > 0) == (a + y > 0))
            if not f:
                flag = False
                break
    if flag:
        print(a)
