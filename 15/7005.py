def UGOL(g, b, c):
    return g + b + c == 180


for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = UGOL(37, a, x + 45) == UGOL(a, x, 90) and (not (a + 23 < 120))
        if not f:
            flag = False
            break
    if flag:
        print(a)
