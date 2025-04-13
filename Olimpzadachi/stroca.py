a = "JATHFAAFJAAKAGATAAT"
d = []
for i in range(len(a) - 1):
    if a[i] == "A":
        bukva = a[i + 1]
        d.append(bukva)
    else:
        continue

gen = [ord(x) for x in d if d.count(x) > 1]
print(gen)


d1 = [0] * 26

for i1 in gen:
    d1[i1 - 65] += 1
print(d1)
print(d1[::-1])
print(chr(-(d1[::-1].index(max(d1))) + 65 - 1))
print(chr(-d1[::-1].index(max(d1)) - 1 + 26 + 65))
