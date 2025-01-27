from fnmatch import *

for a in range(7157, 10 ** 10 + 1, 7157):
    if fnmatch(str(a), "*3185*32"):
        print(a, a// 7157)