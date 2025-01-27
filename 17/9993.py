def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


a = open("17_9993.txt")
b = [int(x) for x in a]
mxe = max([x for x in b if str(x)[-2:] == "17"])
mxp = 0
c = 0
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    prost = [x for x in k if is_prime(x)]
    if len(prost) == 1:
        if (k[0] + k[1]) % mxe == 0:
            c += 1
            mxp = max(mxp, k[0] * k[1])
print(c, mxp)
