from itertools import product

pr = product("0123456789abcdef", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    j = [x for x in h if str(x) >= "9"]
    if h.count("8") == 1:
        if len(j) >= 2:
            c += 1
print(c)
