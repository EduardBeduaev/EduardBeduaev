from itertools import product

pr = product("0123456789abcdef", repeat=3)
c = 0
for i in pr:
    h = "".join(i)
    if h[0] > h[1] and h[1] > h[2]:
        c += 1

pr1 = product("0123456789abcdef", repeat=5)
for i1 in pr1:
    h1 = "".join(i1)
    if h1[0] > h1[1] and h1[1] > h1[2] and h1[2] > h1[3] and h1[3] > h1[4]:
        c += 1
print(c)