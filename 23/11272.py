def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    else:
        return f(a - 3, b) + f(a // 2, b)


print(f(28, 3))
