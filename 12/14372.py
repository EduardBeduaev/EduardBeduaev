for n in range(3, 1001):
    s = ">" + "0" * 25 + "1" * n + "2" * 25
    while ">1" in s or ">2" in s or ">0" in s:
        s = s.replace(">1", "22>",1)
        s = s.replace(">2", "2>", 1)
        s = s.replace(">0", "1>", 1)
    print(n, sum(map(int, s[:-1])))
