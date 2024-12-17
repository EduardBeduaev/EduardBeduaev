for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) or (x & a != 0) or (x & 58 == 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)

