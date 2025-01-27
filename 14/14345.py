for x in "0123456789abcd":
    r = int(f"4b3{x}1", 14) + int(f"5{x}f83",16)
    if r % 13 == 0:
        print(r // 13)