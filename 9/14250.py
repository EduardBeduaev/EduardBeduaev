a = open("14250.txt")
s = num = 0
for i in a:
    num += 1
    b = sorted(map(int, i.split()))
    if len(set(b)) == 6 and (b[-1] + b[0]) ** 3 >= sum(b[1:-1]) ** 2:
        s += num
print(s)