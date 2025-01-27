from itertools import product

pr = product("ДЖОБС", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    if h.count("Д") == 1 and h.count("О") == 1 and h.count("С") == 1:
        if h.count("Ж") <= 2:
            c += 1
print(c)