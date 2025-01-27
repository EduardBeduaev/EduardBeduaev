from itertools import product

pr = product("ГРАНТ", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h == "ГРАНАТ":
        break
print(c)