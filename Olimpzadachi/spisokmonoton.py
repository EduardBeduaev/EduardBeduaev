m = [1, 10, 2, 5]
c = 0
for i in range(len(m) - 1):
    c += 1
    if m[i] > m[i + 1]:
        if c == len(m) - 1:
            print("NO")
    elif c == len(m) - 1:
        print("Yes")

