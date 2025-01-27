a = int(input())
b = [str(a)[x] for x in range(len(str(a)) - 1, -1, -1)]
c = "".join(b)
if str(a) == c:
    print("Круто")
else:
    print("не круто")

