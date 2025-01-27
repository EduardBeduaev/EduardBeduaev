def DEL(n,m):
    return n % m == 0


for a in range(1,400):
    flag = True
    for b in range(10, 81):
        for x in range(1, 400):
            f = DEL(x, a) or (not b or not(DEL(x, 18)))
            if not f:
                flag = False
                break
    if flag:
        print(a)
