for x in "0123456789abcdefghi":
    r = int(f"98{x}79641", 19) + int(f"36{x}14", 19) + int(f"73{x}4",19)
    if r % 18 == 0:
        print(x, r // 18)

#467926120
