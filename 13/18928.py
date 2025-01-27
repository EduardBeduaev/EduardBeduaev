from ipaddress import *

net = ip_network("192.168.248.176/255.255.255.240")
c = 0
for ip in net:
    b = bin(int(ip))[2:]
    if b.count("1") == b.count("0"):
        c += 1
print(c)