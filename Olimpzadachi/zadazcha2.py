#N, K, M = list(map(int, input().split()))


n, k, m = map(int, input().split())
c_d = 0

while n // k != 0:
    c_z = n // k
    ost_z = n - k * c_z
    c_c_d = k // m * c_z
    ost_d = k - (k // m) * m
    n = ost_z + ost_d * c_z
    c_d += c_c_d

print(c_d)
