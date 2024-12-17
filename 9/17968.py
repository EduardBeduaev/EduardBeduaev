a = open("17968.txt")
c = 0
for i in a:
    b = [int(x) for x in i.split()]
    b_c = sorted(b)
    b_chetn = [x for x in b_c if x % 2 == 0]
    b_netch = [x for x in b_c if x % 2 != 0]
    if sum(b_chetn) == sum(b_netch):
        if b_c[-1] < sum(b_c[:-1]):
            c += 1
print(c)
