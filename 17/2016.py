a = open("17_2016.txt")
b = [int(x) for x in a]
d = []
for i in b:
    if i % 13 == 7:
        if i % 7 !=0:
            if i % 11 != 0:
                d.append(i)

r = max(d) - min(d)
print(r, len(d))