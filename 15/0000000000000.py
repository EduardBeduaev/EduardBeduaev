for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = ((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0)
        if not f:
            flag = False
            break
    if flag:
        print(a)