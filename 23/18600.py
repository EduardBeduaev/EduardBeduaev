def f(x, y, p1, p2):
    if x == 30: p1 = 1
    if x == 60: p2 = 1
    if x > y:
        return 0 and 0 < p1 + p2 > 2
    if x == y:
        return 1
    return f(x + 1, y, p1, p2) + f(x * 2, y, p1, p2) + f(x * 3, y, p1, p2)


print(f(10, 70, 0, 0))
