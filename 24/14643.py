a = open("24.13_14643.txt").readline()
a = a.replace("AXMM", "AXM XMM")
a = a.split()
print(len(max(a, key=len)))

