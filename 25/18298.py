from fnmatch import fnmatch

for i in range(1996, 10 ** 10 + 1, 1996):
    if fnmatch(str(i), "1592*6?8"):
        print(i, i // 1996)