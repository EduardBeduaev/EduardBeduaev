for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += "01"
    else:
        b += "10"
    r = int(b, 2)
    if r > 281:
        print(n)