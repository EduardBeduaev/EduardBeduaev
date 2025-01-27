def tri(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(1, 1000):
    t = tri(n)
    if t[-2:] == "10":
        t = "2" + t
    else:
        t = "1" + t
    r = int(t, 3)
    if r > 130:
        print(n)
        break