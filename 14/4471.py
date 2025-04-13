def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 7 * 729**543 - 6 * 81 **765 - 5 * 9 ** 987 - 20
c = 0
for i in f(a, 9):
    if i == 8:
        c += 1
print(c)