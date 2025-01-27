from itertools import product

pr = product("012345678", repeat=7)

for i in pr:
    h = "".join(i)
    i