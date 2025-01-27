for x in "0123456789abcdefghij":
    k1 = int("98897" + x + "21", 19)
    k2 = int("2" + x + "923", 19)
    r = k1 + k2
    if r % 18 == 0:
        print(r // 18)