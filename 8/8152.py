from itertools import product

pr = product("ИКЛНОР", repeat=4)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h == "КИНО":
        print(c)
        break