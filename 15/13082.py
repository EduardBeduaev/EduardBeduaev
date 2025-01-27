for a in range(1,400):
    flag = False
    for x in range(1, 400):
        for y in range(1, 400):
            f = (3 * x + y > 48) or (x > y) or (4 * x + y < a)
            if not f:
                flag = True
                break
    if flag:
        print(a)