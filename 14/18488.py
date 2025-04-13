def f(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]



for x in range(1, 1000):
    a = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    d = f(a, 7)
    c = 0
    for i in d:
        if i == 6:
            c += 1
    if c == 49:
        print(x)
