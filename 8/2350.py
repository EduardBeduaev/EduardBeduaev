from itertools import product

pr = product("123456789", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    if h[0] != "5" and h.count("2") == 2:
        c += 1
print(c)