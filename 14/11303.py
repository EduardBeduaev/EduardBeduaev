for x in "0123456789abcdefghij":
    s = int(f"627{x}J8", 20) + int(f"H45I{x}5HIJ", 20) + int(f"4IDB49J{x}7", 20)
    if s % 19 == 0:
        print(s // 19)