for n in range(224, 1000):
    b = bin(n)[2:]
    s = n - b.count("0")
    s1 = bin(s)[2:]
    s1 = s1[2:] + s1
    r = int(s1, 2)
    if r > 224:
        print(r)
