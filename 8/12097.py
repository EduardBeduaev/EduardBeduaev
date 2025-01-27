from itertools import product

pr = product("АГДИЛНРЯ", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h[0] == "Я" and h.count("Д") != 3:
        print(c)
