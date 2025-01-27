from fnmatch import fnmatch

for n in range(700_000, 1000000):
    if not fnmatch(str(n), "*4??2"):
        if not fnmatch(str(n), "*0??3*"):
            if not fnmatch(str(n), "*1*"):
                if n % 13 == 0:
                    print(n)
