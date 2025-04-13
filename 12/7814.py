for n in range(5, 400):
    s = "2" + "4" * n
    while "14" in s or "244" in s or "444" in s:
        if "14" in s:
            s = s.replace("14", "2", 1)
        if "244" in s:
            s = s.replace("244", "14", 1)
        if "444" in s:
            s = s.replace("444", "21", 1)
    summa = sum(map(int,list(s)))
    if summa > 20:
        print(n)