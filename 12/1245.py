for o in range(1, 27):
    for d in range(1, 55):
        for t in range(1, 47):
            s = "0" + "1" * o + "2" * d + "3" * t + "0"
            while "00" not in s:
                s = s.replace("01", "210", 1)
                s = s.replace("02", "320", 1)
                s = s.replace("03", "3012", 1)
            if s.count("1") == 26 and s.count("2") == "54" and s.count("3") == 46:
                print(s)
