for n in range(1, 1000):
    b = bin(n)[2:]
    if b.count("1") > b.count("0"):
        b += "0"
    else:
        b = "11" + b
    if b.count("1") > b.count("0"):
        b += "0"
    r = int(b, 2)
    if r > 500:
        print(n)
