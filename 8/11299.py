from itertools import product

pr = product("БМНРЮ", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if c % 2 != 0:
        if h[0] != "М" and h.count("Р") >= 2 and h.count("Ю") == 0:
            print(c)