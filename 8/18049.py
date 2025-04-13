from itertools import product

pr = product("012345678", repeat=7)
c = 0
for i in pr:
    h = "".join(i)
    if h[0] != "0" and h[0] != "2" and h[0] != "4" and h[0] != "6":
        if h[-3:] != "000" and h[-3:] != "111" and h[-3:] != "222" and h[-3:] != "333" and h[-3:] != "444" and h[-3:] != "555" and h[-3:] != "666" and h[-3:] != "777" and h[-3:] != "888":
            c += 1
print(c)

