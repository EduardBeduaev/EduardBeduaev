a = open("17_9969.txt")
b = [int(x) for x in a]
raz = [x for x in b if b.count(x) >= 1]
mxe = [abs(x) for x in b if]
for i in range(len(b) - 2):
    k = [b[i], b[i + 1], b[i + 2]]
    polnkwadr = [x for x in k if abs(x) ** 0.5 == int]
    if len(polnkwadr) == 1:
