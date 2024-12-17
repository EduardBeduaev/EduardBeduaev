for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (x & a != 0) <= ((x & 168 == 0) <= (x & 69 != 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)
