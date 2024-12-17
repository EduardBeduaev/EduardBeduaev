print("k l m n")
for k in range(2):
    for l in range(2):
        for m in range(2):
            for n in range(2):
                if not ((k <= m) and (k or n) or (l <= n)):
                    print(k, l, m, n)
