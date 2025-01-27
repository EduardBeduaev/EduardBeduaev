for n in range(3, 1000):
    s = "3" + "7" * n
    while "37" in s or "577" in s or "777" in s:
        if "37" in s:
            s = s.replace("37", "7", 1)
        if "577" in s:
            s = s.replace("577", "73", 1)
        if "777" in s:
            s = s.replace("777", "5", 1)
    summa = sum(map(int, list(s)))
    if len(str(summa)) == 2:
        print(n)