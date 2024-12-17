a = open("17_12735.txt")
b = [int(x) for x in a]
for i in range(len(b) - 1):
    k = [b[i], b[i + 1]]
