f = open("27880.txt")
s,n = map(int, f.readline().split())
vars = sorted([int(x) for x in f])
l = []
for var in vars:
    if sum(l) + var <= s:
        l.append(var)
    else:
        break

print(len(l))


vars.pop()


for i in vars[::-1]:
    if i + sum(l) <= s:
        l.append(i)
        break
print(len(l), l[-1])
