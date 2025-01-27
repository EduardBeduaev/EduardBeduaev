from ipaddress import *

net = ip_network("112.160.0.0/255.240.0.0")
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("1") % 3 != 0:
        c += 1
print(c)