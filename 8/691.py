from itertools import product

pr = product("ВЕКНО", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h.count("Н") == 2 and h.count("К") == 2:
        print(c)
