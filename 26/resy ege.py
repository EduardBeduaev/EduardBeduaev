a = open("27882.txt")

s, n = map(int, a.readline().split())
vars = sorted([int(x) for x in a])

l = []
for var in vars:
    if sum(l) + var <= s:
        l.append(var)
    else:
        break

l.pop()

for i in vars[::-1]:
    if sum(l) + i <= s:
        l.append(i)
        break

print(len(l), l[-1])
