from ipaddress import *

net = ip_network("192.168.32.48/255.255.255.192", 0)
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("1") % 5 != 0:
        c += 1
print(c)