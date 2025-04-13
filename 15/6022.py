for a in range(1,400):
    flag = True
    for x in range(1,400):
        for y in range(1,400):
            f = (x < a) or (y < a) or ( x + 2 * y > 150)
            if not f:
                flag = False
                break
    if flag:
        print(a)