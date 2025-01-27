from ipaddress import *

net = ip_network("136.36.240.16/255.255.255.248")
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if "101" not in b:
        c += 1
print(c)