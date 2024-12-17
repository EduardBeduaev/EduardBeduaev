a = open("17_18617.txt")
b = [int(x) for x in a]
d = []
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
    l = [x for x in k if x % 3 == max(b) % 3]
    c = [x for x in k if x % 7 == min(b) % 7]
    if len(l) >= 1:
        if len(c) >= 1:
            d.append(sum(k))
print(len(d), max(d))
