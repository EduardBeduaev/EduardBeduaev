for n in range(3, 10_001):
    s = "1" + "2" * n
    while "12" in s or "322" in s or "222" in s:
        if "12" in s:
            s = s.replace("12", "2", 1)
        if "322" in s:
            s = s.replace("322", "21", 1)
        if "222" in s:
            s = s.replace("222", "3", 1)
    r = sum(map(int, list(s)))
    if r == 15:
        print(n)
        break
