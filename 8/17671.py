from itertools import product

pr = product("ЛАЙМ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if "М" not in h and "Л" not in h and "ЙЙ" not in h:
        print(c)

