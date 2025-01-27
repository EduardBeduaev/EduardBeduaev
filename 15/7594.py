for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = x & 39 == 0 or ((x & 11 == 0) <= (not (x & a == 0)))
        if not f:
            flag = False
            break
    if flag:
        print(a)
