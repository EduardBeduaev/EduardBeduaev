from itertools import product

pr = product("АБВГЭЮЯ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    if h[0] == "Э" or h[0] == "Ю" or h[0] == "Я":
        if h[-1] == "Э" or h[-1] == "Ю" or h[-1] == "Я":
            c += 1
print(c)