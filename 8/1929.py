from itertools import product

pr = product("ДЕЙКСТРА", repeat=6)
c = 0
for i in pr:
    h = "".join(i)
    razl = [x for x in h if h.count(x) == 1]
    if h.count("Й") == 1:
        if "ЙД" in h or "ЙЙ" in h or "ЙК" in h or "ЙС" in h or "ЙТ" in h or "ЙР" in h:
            if "ЙА" not in h and "ЙЕ" not in h:
                if len(razl) == 6:
                    c += 1
print(c)