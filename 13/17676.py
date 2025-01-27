from ipaddress import *
c = 0
net = ip_network("115.192.0.0/255.192.0.0")
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("1") % 3 != 0:
        c += 1
print(c)