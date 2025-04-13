from itertools import product

pr = product("0123456789ab", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    bolshe8 = [x for x in h if int(x, 12) > 8]
    if h.count("7") == 1:
        if len(bolshe8) <= 3 and h[0] != "0":
            c += 1

print(c)