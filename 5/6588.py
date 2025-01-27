for n in range(1, 1000):
    b = bin(n)[2:]
    s = str(b)
    s = s.replace("0", "2")
    s = s.replace("1", "0")
    s = s.replace("2", "1")
    s = "1" + s
    if s.count("1") % 2 != 0:
        s += "1"
    else:
        s += "0"
    r = int(s, 2)
    if r > 180:
        print(n)
        break
