def chestn(n, ss):
    s = []
    while n > 0:
        s.append(n % ss)
        n //= ss
    return s[::-1]


a = open("17_2017.txt")
b = [int(x) for x in a]
d = []
for i in range(len(b)):
    if b[i] % 16 == 11 and b[i] % 7 == 0 and b[i] % 6 != 0 and b[i] % 13 != 0 and b[i] % 19 != 0:
        d.append(b[i])
print(sum(d), len(d))
