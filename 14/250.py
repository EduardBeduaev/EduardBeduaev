for n in range(1, 41):
    if str(bin(n)[2:])[-4:] == "1011":
        print(n)