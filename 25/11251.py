from fnmatch import fnmatch

for n in range(2291, 10 ** 10 + 1, 2291):
    if fnmatch(str(n), "*222132?"):
        print(n, n // 2291)