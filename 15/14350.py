for a in range(1, 400):
    flag = False
    for x in range(1, 400):
        for y in range(1, 400):
            f = not((x < 7) or (y >= 3 * x + a - 20) or (x >= 34) or (y < 121))
            if f == 0:
                flag = True
                break
    if flag:
        print(a)
