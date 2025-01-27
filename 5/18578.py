def cht(n):
    s = ""
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s


for x in range(1, 10000):
    b = cht(x)
    if x % 4 == 0:
        b = "2" + b + "03"
    else:
        b += cht(x % 4 * 5)
    r = int(b, 4)
    if r < 567:
        print(x)
