from itertools import product
pr = product("КАЛЕЙДОСКОП", repeat=6)
c = 0
b = 0
for i in pr:
    h = "".join(i)
    c += 1
    if c % 2 == 0:
        if h[0] == "К" and h.count("Й") >= 2 and h not in "С" and h not in "Е":
            b += 1
print(b)
