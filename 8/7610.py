from itertools import product

pr = product("АКЛМНЯ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h[0] == "К" and h[1] == "М":
        print(c)