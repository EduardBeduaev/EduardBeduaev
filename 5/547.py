for n in range(1, 1000):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    r = int(b, 2)
    if r > 103:
        print(n)
        break
