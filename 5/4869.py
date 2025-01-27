for n in range(1, 10000):
    b = bin(n)[2:]
    chetn = [b[x] for x in range(len(b)) if x % 2 == 0]
    ncht = [b[x] for x in range(len(b)) if x % 2 != 0]
    r1 = ncht.count("1")
    r2 = chetn.count("0")
    r = abs(r1 - r2)
    if r == 5:
        print(n)
        break

