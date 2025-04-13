for n in range(1,200):
    s = "0" * 40 + "1" * n + "2" * 40
    while "31" in s or "32" in s or "30" in s:
        if "31" in s:
            s = s.replace("31", "223", 1)
        if "32" in s:
            s = s.replace("32", "23", 1)
        if "30" in s:
            s = s.replace("30", "13", 1)
        s = s.replace("3", "0", 1)
    summa = sum(map(int,list(s)))
    check = [x for x in (str(summa)) if len(str(summa)) == 3 and str(summa).count(x) == 3]
    if check:
        print(n)