from math import ceil

a = open("inf_22_10_20_26.txt")

n = 1000  #кол - во купленных товаров
b = sorted([int(x) for x in a])
mens = [x for x in b if x <= 50]
bols = [x for x in b if x > 50]
c = 0

a_b = bols[482:]
a_m = bols[:482]

print(ceil(sum(mens) + sum(a_b) + (sum(a_m) * 3 / 4)))
