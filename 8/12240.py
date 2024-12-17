from itertools import product

pr = product("012345678", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    if h.count(
            "5") == 1 and h not in "00" and h not in "11" and h not in "22" and h not in "33" and h not in "44" and h not in "55" and h not in "66" and h not in "77" and h not in "88":
        c += 1
print(c)
