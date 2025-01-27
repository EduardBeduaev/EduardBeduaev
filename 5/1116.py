for n in range(1, 1000):
    b = bin(n)[2:]
    if b.count("1") == b.count("0"):
        b += b[-1]
    elif b.count("1") > b.count("0"):
        b += "0"
    elif b.count("0") > b.count("1"):
        b += "1"
    if b.count("1") == b.count("0"):
        b += b[-1]
    elif b.count("1") > b.count("0"):
        b += "0"
    elif b.count("0") > b.count("1"):
        b += "1"
    if b.count("1") == b.count("0"):
        b += b[-1]
    elif b.count("1") > b.count("0"):
        b += "0"
    elif b.count("0") > b.count("1"):
        b += "1"
    r = int(b, 2)
    if n < 100:
        if r % 4 == 0 and r % 8 != 0:
            print(n)
