def DEL(n, m):
    return n % m == 0


for a in range(1, 100000):
    flag = True
    for x in range(1, 1000):
        f = not(DEL(x, 263) <= DEL(x, a)) and DEL(x, 71)
        if not f:
            flag = False
            break
    if flag:
        print(a)
