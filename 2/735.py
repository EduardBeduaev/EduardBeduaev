print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not (y and x and (not (z or w)))
                print(x, y, z, w, int(f))
