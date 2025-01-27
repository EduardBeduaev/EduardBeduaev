for x in "0123456789abcdefghijklmnopqrst":
    k = int("49" + x + "42696", 29)
    k1 = int("8" + x + "22", 29)
    r = k + k1
    if r % 28:
        print(r // 28)