print(bin(50)[2:])

def tri(n):
    s = ""
    while n > 0:
        s = str((n % 7)) + s
        n //= 7
    return s

print(tri(50))

