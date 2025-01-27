a = open("24_12476.txt").readline()
a = a.replace("E", " ")
a = a.replace("G", " ")
a = a.replace("R", "*")
a = a.replace("O", "-")
a = a.replace("P", ' ')

while "-*-" in a or "*-*" in a:
    a = a.replace("-*-", ' ')
    a = a.replace("*-*", ' ')

while "-*" in a:
    a = a.replace("-*", " ")

if "*-" in a.split() == 21:
    print(a.split())
