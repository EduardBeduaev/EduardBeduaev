from itertools import product

pr = product("АВНРЬЯ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if (h.count("Ь") <= 1) and ("ЯЯ" not in h) and (h[0] != "Я"):
        print(c)