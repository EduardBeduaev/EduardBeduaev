def f(x, y, Z):
    if x > y + 2:
        return 0
    if x == y:
        return 1
    if Z[-2:] == "AA":
        return f(x + 5, y, Z + "B") + f(x * 2, y, Z + "C")
    return f(x - 1, y, Z + "A") + f(x + 5, y, Z + "B") + f(x * 2, y, Z + "C")


print(f(5, 34, ""))
