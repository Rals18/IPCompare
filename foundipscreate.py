import ipaddress
#create founds_ip and found_ip text files using found_ip_list
#creates the numerical value ranges for IPs in order to easily compare
def cidr_range_to_numbers(cidr_range):
    ip_network = ipaddress.ip_network(cidr_range, strict=False)
    start_ip = int(ip_network.network_address)
    end_ip = int(ip_network.broadcast_address)
    return start_ip, end_ip

ip = open("found_ip_list.txt",'r')
cidr_rangee = ip.read()
cidr_ranges = cidr_rangee.split("\n")
ip.close()

ips = open("founds_ip.txt",'w')
for cidr_range in cidr_ranges:
    start_ip, end_ip = cidr_range_to_numbers(cidr_range)
    print ("{}".format(cidr_range), "{}".format(start_ip), "{}".format(end_ip), file=ips)
ips.close()
