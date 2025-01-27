from itertools import product

pr = product("ЕКМОПРТЬЮ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h.count("К") == 2 and h[0] not in "Ь":
        if c % 2 != 0:
            print(c)
