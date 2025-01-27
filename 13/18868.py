from ipaddress import *

net = ip_network("222.121.128.0/255.255.224.0")
c = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b[-2:] == "11" or b[-2:] == "00":
        c += 1
print(c)