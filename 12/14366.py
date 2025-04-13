for n in range(3,10_001):
    s = "9" + "6" * n
    while "95" in s or "6666" in s or "1166" in s:
        if "96" in s:
            s = s.replace("96", "11", 1)
        if "6666" in s:
            s = s.replace("6666", "9", 1)
        if "1166" in s:
            s = s.replace("1166", "69", 1)
    summa = sum(map(int, list(s)))
    if summa % 37 == 0:
        print(n)