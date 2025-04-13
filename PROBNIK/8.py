from itertools import product

pr = product("012345678", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    nechetn = [x for x in h if int(x) % 2 != 0]
    if h[0] != "0" and h.count("4") == 1:
        if len(nechetn) == 2:
            c += 1

print(c)
#53760