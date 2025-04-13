def f(m, n):
    return m & n


for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f1 = (f(x, a) != 0) <= ((f(x, 168) == 0) <= (f(x, 69) != 0))
        if not f1:
            flag = False
            break
    if flag:
        print(a)
