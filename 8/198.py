from itertools import product
pr = product("НИЧЬЯ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    if h[0] != "Ь" and h.count("ЬИЯ") == 0:
        if h.count("Ь") == 1 and h.count("И") == 1 and h.count("Н") == 1 and h.count("Ч") and h.count("Я") == 1:
            c += 1
print(c)
