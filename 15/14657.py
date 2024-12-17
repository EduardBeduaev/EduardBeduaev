def DEL(n, m):
    return n % m == 0


for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = ((not DEL(x, 17)) or (not DEL(x, 12))) <= (not DEL(x, a))
        if not f:
            flag = False
            break
    if flag:
        print(a)
