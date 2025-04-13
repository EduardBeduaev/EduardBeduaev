def wif(x,y):
    return str(x)[-1] == str(y)[-1]

for a in range(1,400):
    flag = True
    for x in range(1,400):
        f = (not (wif(x,5)) and (wif(x,4))) <= (x > a - 11)
        if not f:
            flag = False
            break
    if flag:
        print(a)