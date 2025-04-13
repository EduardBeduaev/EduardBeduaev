print("x y z w F1 F2")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w == x) and (y <= z)
                f1 = (w <= x) <= (y == z)
                print(x,y,z,w, int(f), int(f1))
