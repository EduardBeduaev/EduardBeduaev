b = []
for p in range(6,37):
    num1 = int("24351", p)
    b.append(num1)
a = []
for q in range(6, 37):
    num2 = int("14325", q)
    a.append(num2)

for i in a:
    for i1 in b:
        if i == i1:
            print(i)

