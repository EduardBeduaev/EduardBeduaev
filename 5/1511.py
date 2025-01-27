for n in range(1, 1000):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    r = int(b, 2)
    if 64 < r < 72:
        print(n)