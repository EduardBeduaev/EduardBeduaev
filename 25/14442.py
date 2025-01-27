from fnmatch import fnmatch

for i in range(2068,10 ** 9, 2068):
    if fnmatch(str(i), "193*7?"):

            print(i)