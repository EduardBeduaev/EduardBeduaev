from itertools import product

pr = product("ОДЕКОЛОН", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    if "ОО" not in h and "ДД" not in h and "ЕЕ" not in h and "КК" not in h and "ЛЛ" not in h and "НН" not in h:
        c += 1
print(c)