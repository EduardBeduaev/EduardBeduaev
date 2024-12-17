def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


a = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024

print(f(a,25))