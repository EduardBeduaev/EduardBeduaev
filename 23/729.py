def f(x, y):
    if x > y or x == 12:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y)

print(f(7,27) * f(27, 50))