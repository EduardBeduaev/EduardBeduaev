from itertools import product

pr = product("0123456789abcd", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    razl = [x for x in h if h.count(x) == 1]
    if len(set(h)) == 2 and h[0] != "0":
        if h[-1] in "03":
            c += 1
print(c)