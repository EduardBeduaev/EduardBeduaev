

def f(x, y):
    if x > y or x == 23 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29 or x == 31:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


print(f(8,16 ) * f(16,32))
