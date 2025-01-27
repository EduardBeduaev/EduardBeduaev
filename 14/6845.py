for x in "0123456789abcdefghijklmnqp":
    for y in "0123456789abcdefghijklmnqp":
        if int(f"1{x}77", 27) + int(f"{x}{x}77", 27) == int(f"{y}0{y}{y}", 27):


