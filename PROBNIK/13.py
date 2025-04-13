from ipaddress import *

net = ip_network("192.168.32.160/255.255.255.240")
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(8)
    if b.count("1") % 2 == 0:
        c += 1
print(c)
#8
