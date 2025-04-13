for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = ((x & 116 != 0) or (x & 92 != 0)) <= ((x & 69 == 0) <= (x & a != 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)