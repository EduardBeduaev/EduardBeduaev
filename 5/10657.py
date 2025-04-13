def tri(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s


for t in range(1, 1000):
    troi = tri(t)
    check = sum([int(x) for x in troi if str(x) != "0"])
    if check % 3 == 0:
        troi = "20" + troi
    else:
        troi = "10" + troi
    r = int(troi, 3)
    if r < 100:
        print(t)
