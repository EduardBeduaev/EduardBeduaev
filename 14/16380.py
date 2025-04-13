def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024
c = 0

for i in f(a, 25):
    if i > 10:
        c += 1
print(c)