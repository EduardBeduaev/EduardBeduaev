a, b, a1, b1 = list(map(int, input().split()))


#2
def func2():
    spisok = [[a, a1, b, b1], [a, b1, a1, b], [b, a1, b1, a], [b, b1, a, a1]]
    s = []
    for i in spisok:
        storona1 = i[0] + i[1]
        if i[2] <= i[3]:
            storona2 = i[3]
        else:
            storona2 = i[2]
        s.append([storona1, storona2])
    return s


func2 = func2()
b = []
for i in func2:
    b.append(i[0] * i[1])

minznach = min(b)
mnoz = set()
for i in func2:
    if i[0] * i[1] == minznach:
        if i[0] == i[1]:
            print(i[0], i[1])
        else:
            a = (i[0], i[1])
            b = (i[1], i[0])
            mnoz.add(a)
            mnoz.add(b)

for i in mnoz:
    print(*i)