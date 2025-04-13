from fnmatch import fnmatch

for i in range(237, 10 ** 8 + 1):
    if fnmatch(str(i), "81?2*80"):
        print(i, i // 237)
