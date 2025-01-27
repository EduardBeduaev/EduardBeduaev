from ipaddress import *
c = 0
uz = "76.155.48.0".zfill(32)
ipa = "76.155.48.2".zfill(32)
for mask in range(33):
    net = ip_network(f"{ipa}/{mask}")
    if net.network_address == ip_address(f"{ipa}"):
        c += 1
print(c)