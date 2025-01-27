from itertools import product

pr = product("ПУЛЯ", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    if h.count("У") == 2:
        c += 1
print(c)