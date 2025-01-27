for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        for p in range(13, 19):
            for q in range(17, 23):
                f = not (not ((x == p) <= (x == q))) <= ((x == a) <= (not((x == q) <= (x == p))))
                if not f:
                    flag = False
                    break
    if flag:
        print(a)