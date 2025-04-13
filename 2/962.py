print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((w or x or (not z) or y) and (w or x or (not z) or (not y)) and (w or (not x) or (not z) or (not y))):
                    print(x,y,z,w)