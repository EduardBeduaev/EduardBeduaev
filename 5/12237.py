for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += b[-2] + b[-1]
    else:
        b = "1" + b + "0"
    r = int(b, 2)
    if r < 100:
        print(n)
