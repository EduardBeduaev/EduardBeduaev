from itertools import product

pr = product("АКМСУ", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    c += 1
    if h == "КУМАС":
        print(c)