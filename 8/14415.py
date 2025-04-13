from itertools import product

pr = product("0123456789ab", repeat=5)
c = 0
for i in pr:
    h = "".join(i)
    if h[0] != "0" and h.count("a") == 2:
        if "70" not in h and "72" not in h and "74" not in h and "76" not in h and "78" not in h and "7a" not in h:
            if "07" not in h and "27" not in h and "47" not in h and "67" not in h and "87" not in h and "a7" not in h:
                c += 1
print(c)
