
def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


a = 2 * 729 ** 333 + 2 * 243 ** 333 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338

b = f(a, 9)
c = 0
for i in b:
    if i != 0:
        c += 1
print(c)
