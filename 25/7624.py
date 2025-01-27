from fnmatch import fnmatch

for n in range(2025, 10 ** 10, 2025):
    if fnmatch(str(n), "21?5846*"):
        print(n, n // 2025)