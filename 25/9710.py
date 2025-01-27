from fnmatch import fnmatch

b = []
d = []
for n in range(1_000_001_268, 10 ** 10 - 1, 2023):
    if fnmatch(str(n), "1*1"):
        if n % 2023 == 0:
            b.append(n)
            print(b)
