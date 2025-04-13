for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 5 == 0:
        b += b[-3:]
    else:
        b += bin((n % 5) * 5)[2:]
    r = int(b, 2)
    if r > 256:
        print(n)