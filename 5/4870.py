d = []
for n in range(300, 401):
    b = sorted(str(n))
    if b[0] != "0":
        mn = b[0] + b[1]
        mx = b[-1] + b[1]
    elif b[0] == 0 and b[1] == 0:
        mx = b[-1] + b[1]
        mn = b[-1] + b[1]
    else:
        mn = b[1] + b[0]
        mx = b[-1] + b[1]
    r = int(mx) - int(mn)
    if r == 20:
        d.append(n)
print(len(d))