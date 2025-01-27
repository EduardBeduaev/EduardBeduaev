from fnmatch import fnmatch

for n in range(2024, 10 ** 10, 2024):
    if fnmatch(str(n), "1?2*4"):
        print()