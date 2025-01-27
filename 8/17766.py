from itertools import product

pr = product("БЕНРСТЬЯ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h[0] == "Р" and h.count("Ь") == 0:
        if c % 2 == 0:
            print(c)
