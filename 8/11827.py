from itertools import product

pr = product("01234567", repeat=7)
c = 0
for i in pr:
    h = "".join(i)
    chetn = [x for x in h if int(x,8) % 2 == 0]
    if h[0] != "0" and len(chetn) == 2:
        if "71" not in h and "73" not in h and "77" not in h and "75" not in h:
            if "17" not in h and "73" not in h and "75" not in h and "77" not in h:
                c += 1
print(c)