from itertools import product

pr = product("ПРОБНИК", repeat=7)
c = 0
for i in pr:
    h = "".join(i)
    if h[0] != "И" and h[0] != "О":
        if h[-1] != "И" and h[-1] != "О":
            if "ИИ" not in h and "ОО" not in h and "ОИ" not in h and "ИО" not in h:
                c += 1
print(c)