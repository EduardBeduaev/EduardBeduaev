def f(n):
    if n <= 3:
        return 1
    if n % 3 == 0 and n > 3:
        return f(n / 3) + 4 * n
    if n % 3 != 0 and n > 3:
        return n * n * n - 26

for n in range(1, 400):
    if f(n) < 300:
        print(n)