a = open("24_7272 (1).txt").readline()
a = a.replace("AB", "-")
a = a.replace("CB", "-")

while "C" in a or "B" in a or "A" in a:
    a = a.replace("A", " ")
    a = a.replace("B", " ")
    a = a.replace("C", " ")

a = a.split()
print(len(max(a, key=len)))
#ABCBBCBA
#*, ,-, ,, ,
#AB C AB
