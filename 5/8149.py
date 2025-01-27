for n in range(1, 1000):
    b = bin(n)[2:]
    if b.count("1") % 3 == 0:
        b += b[2:]
    else:
        b = b + bin((b.count("1") % 3) * 3)[2:]
    r = int(b, 2)
    if r <= 60:
        print(n)
        break