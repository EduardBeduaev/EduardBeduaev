from itertools import product

pr = product("АВЛОР", repeat=4)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h[0] == "Л":
        print(c)
        break