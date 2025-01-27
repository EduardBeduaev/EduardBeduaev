from itertools import product

pr = product("КРОВЬ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    if "Ь" not in h[0] and "ЬО" not in h and "ОЬ" not in h:
        if h.count("К") == 1 and h.count("Р") == 1 and h.count("О") == 1 and h.count("В") == 1 and h.count("Ь") == 1:
            c += 1
print(c)