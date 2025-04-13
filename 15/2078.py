for a in range(1,400):
    flag = True
    for x in range(1,400):
        f = (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)