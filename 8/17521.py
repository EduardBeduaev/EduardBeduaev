from itertools import product

pr = product("01234567", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    if h[0] != "1" and h[0] != "3" and h[0] != "5" and h[0] != "7":
        if h.count("7") <= 2:
            if h[-1] != "6" and h[-1] != "2":
                c += 1
print(c)