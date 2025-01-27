for x in "0123456789abcdefghijk":
    k = int(f"56{x}c20", 22) + int(f"89f{x}2", 22) + int(f"h24{x}k21", 22)
    if k % 21 == 0:
        print(x, k // 21)