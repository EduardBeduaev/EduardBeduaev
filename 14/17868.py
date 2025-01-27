d = []
for x in "0123456789abcdefghi":
    k1 = int(f"98897{x}21", 19) + int(f"2{x}923", 19)
    if k1 % 18 == 0:
        print(x, k1// 18)