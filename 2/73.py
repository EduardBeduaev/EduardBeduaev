print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not (x and y and not (z or x and not y)) and not w)
                print(x, y, z, w, int(f))
