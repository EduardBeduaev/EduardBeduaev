from itertools import product

pr = product("0123456789abcdefghijklmnop", repeat=4)

for i in pr:
    h = "".join(i)
    if h.count("1")
