from itertools import product

pr = product("АПРСУ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h.count("У") <= 1:
        if "АА" not in h:
            print(c)