def DEL(m, n):
    return n % m == 0


def samboll(s, d):
    if (d + s) > 0:
        return s + d


for a in range(1, 400):
    flag = True
    for x in range(1, 400):
        f = (x + a >= 160) or (DEL(x, 7) >= (not samboll(x, -17)))
        if not f:
            flag = False
            break
    if flag:
        print(a)
