for x in "0123456789abcdefghijklmnqp":
    k = int(f"123{x}24",27) + int(f"135{x}78", 27)
    if k % 26 == 0:
        print(x, k//26)