for n in range(1, 1000):
    b = bin(n)[2:]
    s = str(b)
    s += str(b.count("1") % 2)
    s += str(b.count("1") % 2)
    r = int(s, 2)
    if r < 80:
        print(n)