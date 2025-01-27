for x in "0123456789abcdefghijklmno":
    k = int(f"11353{x}12", 25) + int(f"135{x}21", 25)
    if k % 24 == 0:
        print(x, k // 24)
