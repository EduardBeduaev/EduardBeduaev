from ipaddress import *

net = ip_network("214.96.0.0/255.240.0.0")
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(8)
    if b.count("0") % 3 == 0:
        c += 1
print(c)