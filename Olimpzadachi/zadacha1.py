x, y, z = list(map(int, input().split()))
#1 месяц # 2 день либо наоборот , #3 год


if 12 < x < 31:
    print(1)
elif 12 < y < 31:
    print(1)
else:
    print(0)
