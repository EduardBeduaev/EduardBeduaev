c = 0
for a in range(-500, 500):
    flag = True
    for x in range(-500, 500):
        for y in range(-500, 500):
            f = ((a < x) or (x ** 2 - 7 * x + 10 > 0)) and ((a >= y) or (y ** 2 + 7 * y + 12 > 0))
            if not f:
                flag = False
                break
        if not flag:
            break
    if flag:
        c += 1
        print(c)
