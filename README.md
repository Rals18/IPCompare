# IPCompare
IP Comparer Program
Nikul Maloo, nikul.maloo@gmail.com

This project allows one to use a list of IP addresses(/16s) and a list of companies and find new IPs that are not in the list of IP addresses provided and belong to a company mentioned in the list.
The function of certain lines of code are explained within the files themselves.

Files needed:
1. List of companies included in a text file
    EX. SPRINT
        ATT
2. get-pip.py(downloadable)
3. Text file containing one list of /16 ips (included as file 256-ipblocks.txt for your convenience)
    EX. 256.0.0.0/16
        256.1.0.0/16
        ...
        256.255.0.0/16
4. Python(downloadable)

How to run code:
1. To run create.py - python3 create.py (will create a text file for every single list of /16 IPs)
2. To run main.py - python3 main.py -i 256-ipblocks.txt
(256 can be replaced by the current list of IPs you are running)
3. To run foundipscreate.py - python3 foundipscreate.py
4. To run newipscreate.py - python3 newipscreate.py
5. To run ip_compare.py - python3 ip_compare.py

*Advised to run code in order, for best experience*

Known Bugs:
When running foundipscreate.py and newipscreate.py occasionally, the code will send back an error for the very last line of the text file, but code still does its job, check new_ips.txt and founds_ip.txt to make sure program has run properly.
