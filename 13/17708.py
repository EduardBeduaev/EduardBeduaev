from ipaddress import *

net = ip_network("211.46.0.0/255.255.128.0")
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("1") % 4 == 0 and b[-2:] == "11":
        c += 1
print(c)