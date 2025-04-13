def con(m, n):
    return m & n

for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = ((con(x,26) != 0) or (con(x, 13) != 0)) <= ((con(x,29) == 0) <= (con(x, a) !=0))
        if not f:
            flag = False
            break
    if flag:
        print(a)