def f(n,ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


a = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029
b = f(a, 27)
d = []
for i in b:
    if i > 9:
        d.append(i)
print(len(d))