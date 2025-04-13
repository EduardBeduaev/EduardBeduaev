def f(n):
    if n < 3:
        return 1
    if n % 2 == 0 and n > 2:
        return f(n - 1) - f(n - 2)
    if n % 2 != 0 and n > 2:
        return f(n - 1) + f(n // 2)


print(f(100))
