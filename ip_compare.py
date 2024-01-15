#create a text file that is seperated by line
nIP = open('new_ips.txt','r')
neIP = nIP.read()
newIP = neIP.split("\n")
nIP.close()

fIP = open("founds_ip.txt",'r')
foIP = fIP.read()
foundIP = foIP.split("\n")
fIP.close()

#Using the text file with all IPs you have, you will be able to see what IPs are new
finding = open("ips_found.txt",'w')
for ip in newIP:
    atEnd=True
    ip = ip.split()
    for found in foundIP:
        found = found.split()
        if int(ip[1]) in range(int(found[1]), int(found[2])):
            atEnd=False
            break
    if atEnd:
        print("Found a new IP", ip[0])
finding.close()
