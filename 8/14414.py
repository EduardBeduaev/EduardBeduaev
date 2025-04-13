from itertools import product

pr = product("012345678", repeat=7)
c = 0
for i in pr:
    h = "".join(i)
    if h.count("6") == 1 and h[0] != "0":
        for g in h:
            if int(g) % 2 == 0:
                h.replace(g, "*")
            else:
                h.replace(i,"-")
                if "**" not in h and "--" not in h:
                    c += 1
print(c)


