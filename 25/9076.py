from fnmatch import fnmatch

for n in range(2023, 10 ** 9, 2023):
    if fnmatch(str(n), "20*23"):
        summa = sum(map(int, list(str(n))))
        if summa % 7 == 0 and summa < 20:
            print(n)
