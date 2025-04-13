a = open("24_105.txt").readline()
a = a.replace("F", " ")
a = a.replace("A", " ")
a = a.replace("I"," ")
a = a.split()
print(len(max(a, key=len)))
#75 СИМВОЛОВ А
#61 символ F
# 31 символов I
#58 cимволов L

