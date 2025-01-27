from ipaddress import *

net = ip_network("172.16.128.0/255.255.192.0")
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("1") % 2 != 0:
        c += 1
print(c)