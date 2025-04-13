from itertools import product

pr = product("0123456", repeat=7)
c = 0
for i in pr:
    h = "".join(i)
    chetn = [x for x in h if int(x, 7) % 2 == 0]
    if h[0] != "0" and len(chetn) == 2:
        c += 1

print(c)