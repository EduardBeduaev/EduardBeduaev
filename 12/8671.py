for m in range(1,1000):
    s = "4" + "6" * m
    while "46" in s or "666" in s:
        if "46" in s:
            s = s.replace("46", "5", 1)
        if "666" in s:
            s = s.replace("666", "4", 1)
    summa = sum(map(int, list(s)))
    if summa > 1000:
        print(m)