def POZ(n,m):
    if n - m > 0:
        return True
    else:
        return False

for a in range(1,400):
    flag = True
    for x in range(1, 400):
        for y in range(1, 400):
            f = not(POZ(x + y, 73)) or not(POZ(37,x - y)) or POZ(y, a)
            if not f:
                flag = False
                break
    if flag:
        print(a)