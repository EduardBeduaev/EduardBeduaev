from itertools import product
c = 0
pr = product("АЕКНС", repeat=6)
for i in pr:
    h = "".join(i)
    c += 1
    if h == "СЕНЕКА":
        print(c)