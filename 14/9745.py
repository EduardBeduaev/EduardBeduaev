from string import ascii_lowercase
alf = "0123456789" + ascii_lowercase

for x in alf[:19]:
    num = int(f"98{x}79641", 19) + int(f"36{x}14", 19) + int(f"73{x}4", 19)
    if num % 18 == 0:
        print(x, num // 18)