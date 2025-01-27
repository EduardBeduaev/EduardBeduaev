a = open("69927.txt")
b = [int(x) for x in a]

for i in range(len(b) - 1):
    k = [b[i], b[i+1]]
    otr = [x for x in k if k.count(x) == 1]
