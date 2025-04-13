for n in range(1, 1000):
    b = bin(n)[2:]
    b = b + b[:2][::-1]
    r = int(b, 2)
    if r > 74:
        print(n)
        break

b1 = "abcd"
b1 = b1 + b1[:2][::-1]
print(b1)
#19