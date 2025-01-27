def f(x):
    s = ""
    while x > 0:
        s += str(x % 6)
        x = x // 6
    return s[::-1]


a = 2 * 216 ** 8 + 4 * 36 ** 12 + 6 ** 15 - 1296
c = f(a)
print(c)
#14