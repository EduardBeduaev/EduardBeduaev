def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]

a = 5 * 343**2031 + 4 * 49**2142 - 3 * 7 ** 111 + 7 ** 222

b = f(a,7)
print(sum(b))