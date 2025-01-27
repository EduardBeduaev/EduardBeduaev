from itertools import product

pr = product("КОСУФ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h.count("Ф") == 0 and h.count("У") == 2:
        print(c)
