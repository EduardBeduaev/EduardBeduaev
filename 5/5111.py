for n in range(1, 1000):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "10" + b[2:] + "1"
    else:
        b = "1" + b[2:] + "11"
    r = int(b, 2)
    if r >= 100:
        print(n)
        break