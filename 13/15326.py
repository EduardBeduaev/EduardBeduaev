from ipaddress import *

net = ip_network("105.224.200.224/255.255.255.224")
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("1") % 4 == 0:
        c += 1
print(c)