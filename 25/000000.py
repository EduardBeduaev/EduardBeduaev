from fnmatch import fnmatch

for i in range(18579,10 ** 10 + 1):
    if fnmatch(str(i), "54?1?3*7"):
        if i % 18579 == 0:
            print(i, i // 18579)