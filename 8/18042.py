from itertools import product

pr = product("ЛЮСТРА", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    if h.count("Ю") <= 2:
        if h[-1] != "Л" and h[-1] != "С" and h[-1] != "Т" and h[-1] != "Р":
            c += 1
print(c)