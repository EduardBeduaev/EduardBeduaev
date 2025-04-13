for x in "0123456789abcdefghijklmnqpgrstuvwxy":
    for y in "0123456789abcdefghijklmnqpgrstuvwxy":
        if int(f"1{x}77", 35) + int(f"{x}{x}77", 35) == int(f"{y}0{y}{y}", 35):
            print(int(f"{y}0{y}{y}", 27))
