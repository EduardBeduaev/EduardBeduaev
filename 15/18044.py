for a in range(1,400):
    flag = False
    for x in range(1,400):
        for n in range(54,77):
            for m in range(32,69):
                f = not((x == m) or (x == n)) == (not(x == a))
                if not f:
                    flag = False
                    break
    if flag:
        print(a)
        break