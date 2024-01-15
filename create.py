#Use this to create a list of all /16 IPs
ip_list = open('256-ipblocks.txt', 'r')
ips = ip_list.read()
allip = ips.split('\n')
ip_list.close()
for x in range(256):
    fname=str(x)+"-ipblocks.txt"
    newIPList = open(fname, "w")
    for ip in allip:
        newIP = ip.replace("256", str(x), 1)
        print(newIP, file=newIPList)
    newIPList.close()
