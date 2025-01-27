from ipaddress import *

net = ip_network("203.111.195.0/255.255.240.0", 0)
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("0") % 3 == 0 and "111" in b and "000" in b:
        c += 1
print(c)