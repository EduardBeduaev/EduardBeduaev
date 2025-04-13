for x in "0123456789abcde":
    m = int(f"432{x}3", 15)
    n = int(f"86{x}86", 15)
    for a in range(1, 1000000):
        if (m + a) % n == 0:
            print(a)
