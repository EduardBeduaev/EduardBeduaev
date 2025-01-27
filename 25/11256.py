from fnmatch import *

for a in range(2476, 10 ** 9 + 1, 2476):
    if fnmatch(str(a), "?2?5554*"):
        print(a, a // 2476)