def prost(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return n


for c in range(6080068, 6080176 + 1):
    pro = prost(c)
    if pro:
        print(c)
