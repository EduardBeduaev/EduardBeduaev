for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = (x > 56) or (y >= x) or (3 * x - y < a)
            if not f:
                flag = False
                break
    if flag:
        print(a)