from ipaddress import *
for mask in range(33):
    net = ip_network(f"222.190.122.24/{mask}", 0)
    if net.network_address == ip_address("222.190.120.0"):
        print(net.num_addresses)