import sys
import getopt
import whoisit
import pprint

inputfile=''
outputfile=''
ipcatch = ''
#sets input and output files to empty strings
try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:",["ifile="])
    #sys.argv has command line args and hi is the short option while ifile is long option, stores these to opts and args
except getopt.GetoptError:
    print("python mywhois.py -i <inputfile>")
    sys.exit(2)
    #indicates that script is being used incorrectly, sys exits with a value of 2 showing that an error occured
for opt, arg in opts:
    if opt == '-h':
        print("python mywhois.py -i <inputfile>")
        sys.exit()
        #-h is the help option and tells the user how to use -i and -h, sys exits with value of zero to show success
    elif opt in ("-i", "-ifile"):
        inputfile = arg
        outputfile = inputfile.replace('.txt', '-out.txt')
        ipcatch = inputfile.replace(".txt", "-catch.txt")
        #the name of inputfile is set to the name of the arg, output file is set to same name as input file but the ending is -out.txt instead of .txt
print("Input file:  ", inputfile)
print("Output file: ", outputfile)
print("IP Catcher: ", ipcatch)
#prints names of input and output files
my_file = open(inputfile, 'r')
#opens the inputfile to be read
data = my_file.read()
#reads the file and stores all data in the variable data
ip_list = data.split('\n')
#splits data(IPs) into multiple lines and stores to ip_list
my_file.close()
#the input file is closed
whoisit.bootstrap()
#initializes the API
my_file = open(outputfile, 'w')
ip_file = open(ipcatch, 'w')
comp_name = open("att-companies.txt", 'r')
a = comp_name.read()
name_list = a.split('\n')
comp_name.close()
#opens the output file to be opened for writing
for x in ip_list: #iterates through each IP adress in the variable
    print("-------- ",x," --------") #prints the IP with dashes on both sides
    try:
        response=whoisit.ip(x)
        #performs a whois query to get info related to this IP
    except:
        print("******** No data for ", x)
        print("******** No data for ", x, file=my_file)
        continue
        #prints No data and uses continue to continue on in the for loop
    print("-------- ",x," --------", file=my_file) #sends info on the IP to the output outputfile
    print(response['handle'], response['name'], response['network'], response['parent_handle'], file=my_file)
    #prints various info about the IP and sends that info to the output file
    cur_out=[]
    if "abuse" in response['entities']:
        #checks if entities has the abuse key
        if "email" in response['entities']['abuse'][0]:
            #checks if email is in abuse(if there are multiple, we only check for first one)
            print(response['entities']['abuse'][0]['email'], end=',', file=my_file)
            #writes the email to the output file seperated by a comma
            cur_out.append(response['entities']['abuse'][0]['email'])
            #adds abuse email to cur.out list
        else:
            print("-", end=',', file=my_file)
            #prints a dash shwoing that an email is not present
        if "handle" in response['entities']['abuse'][0]:
            #checks if handles is in abuse(if there are multiple, we only check for first one)
            print(response['entities']['abuse'][0]['handle'], end=',', file=my_file)
            #writes the handle to the output file seperated by a comma
            cur_out.append(response['entities']['abuse'][0]['handle'])
            #adds abuse handle to cur.out list
        else:
            print("-", end=',', file=my_file)
            #prints a dash to show that a handle is not present
        if "name" in response['entities']['abuse'][0]:
            #checks if name is in abuse(if there are multiple, we only check for first one)
            print(response['entities']['abuse'][0]['name'], file=my_file)
            #writes the name to the output file seperated by a comma
            cur_out.append(response['entities']['abuse'][0]['name'])
            #adds abuse name to cur.out list
        else:
            print("-", file=my_file)
            #prints a dash showing that there is no name
    else:
        print("No abuse data", file=my_file)
        #prints this if no abuse data is present and sends info to output file
        cur_out.append("No data")
        #adds a string saying no data to cur.out list
    if "administrative" in response['entities']:
        #checks if entities has the administrative key
        if "email" in response['entities']['administrative'][0]:
            #checks if email is in administrative(if there are multiple, we only check for first one)
            print(response['entities']['administrative'][0]['email'], end=',', file=my_file)
            #writes the email to the output file seperated by a comma
            cur_out.append(response['entities']['administrative'][0]['email'])
            #adds administrative email to cur.out list
        else:
            print("-", end=',', file=my_file)
            #prints a dash shwoing that an email is not present
        if "handle" in response['entities']['administrative'][0]:
            #checks if handle is in administrative(if there are multiple, we only check for first one)
            print(response['entities']['administrative'][0]['handle'], end=',', file=my_file)
            #writes the handle to the output file seperated by a comma
            cur_out.append(response['entities']['administrative'][0]['handle'])
            #adds administrative handle to cur.out list
        else:
            print("-", end=',', file=my_file)
            #prints a dash shwoing that a handle is not present
        if "name" in response['entities']['administrative'][0]:
            #checks if name is in administrative(if there are multiple, we only check for first one)
            print(response['entities']['administrative'][0]['name'], file=my_file)
            #writes the name to the output file seperated by a comma
            cur_out.append(response['entities']['administrative'][0]['name'])
            #adds administrative name to cur.out list
        else:
            print("-", file=my_file)
            #prints a dash shwoing that a name is not present
    else:
        print("No administrative data", file=my_file)
        #prints this if no administrative data is present and sends info to output file
        cur_out.append("No data")
        #adds a string saying no data to cur.out list

    if "registrant" in response['entities']:
        #checks if entities has the registrant key
        if "email" in response['entities']['registrant'][0]:
            #checks if email is in registrant(if there are multiple, we only check for first one)
            print(response['entities']['registrant'][0]['email'], end=',', file=my_file)
            #writes the email to the output file seperated by a comma
            cur_out.append(response['entities']['registrant'][0]['email'])
            #adds registrant email to cur.out list
        else:
            print("-", end=',', file=my_file)
            #prints a dash shwoing that a email is not present
        if "handle" in response['entities']['registrant'][0]:
            #checks if handle is in registrant(if there are multiple, we only check for first one)
            print(response['entities']['registrant'][0]['handle'], end=',', file=my_file)
            #writes the handle to the output file seperated by a comma
            cur_out.append(response['entities']['registrant'][0]['handle'])
            #adds registrant handle to cur.out list
        else:
            print("-", end=',', file=my_file)
            #prints a dash shwoing that a handle is not present
        if "name" in response['entities']['registrant'][0]:
            #checks if name is in registrant(if there are multiple, we only check for first one)
            print(response['entities']['registrant'][0]['name'], file=my_file)
            #writes the name to the output file seperated by a comma
            cur_out.append(response['entities']['registrant'][0]['name'])
            #adds registrant name to cur.out list
        else:
            print("-", file=my_file)
            #prints a dash shwoing that a name is not present
    else:
        print("No registrant data", file=my_file)
        #prints this if no registrant data is present and sends info to output file
        cur_out.append("No data")
        #adds a string saying no data to cur.out list

    if "technical" in response['entities']:
        #checks if entities has the techincal key
        if "email" in response['entities']['technical'][0]:
            #checks if email is in technical(if there are multiple, we only check for first one)
            print(response['entities']['technical'][0]['email'], end=',', file=my_file)
            #writes the email to the output file seperated by a comma
            cur_out.append(response['entities']['technical'][0]['email'])
            #adds technical email to cur.out list
        else:
            print("-", end=',', file=my_file)
            #prints a dash shwoing that a email is not present
        if "handle" in response['entities']['technical'][0]:
            #checks if handle is in technical(if there are multiple, we only check for first one)
            print(response['entities']['technical'][0]['handle'], end=',', file=my_file)
            #writes the handle to the output file seperated by a comma
            cur_out.append(response['entities']['technical'][0]['handle'])
            #adds technical handle to cur.out list
        else:
            print("-", end=',', file=my_file)
            #prints a dash shwoing that a handle is not present
        if "name" in response['entities']['technical'][0]:
            #checks if name is in technical(if there are multiple, we only check for first one)
            print(response['entities']['technical'][0]['name'], file=my_file)
            #writes the name to the output file seperated by a comma
            cur_out.append(response['entities']['technical'][0]['name'])
            #adds technical name to cur.out list
        else:
            print("-", file=my_file)
            #prints a dash shwoing that a name is not present
    else:
        print("No technical data", file=my_file)
        #prints this if no technical data is present and sends info to output file
        cur_out.append("No data")
        #adds a string saying no data to cur.out list

    str_out=''.join(cur_out)
    #make cur_out list a string
    str_out = str_out.upper()
    #make string all uppercase
    for y in name_list:
        y=y.upper()
        if str_out.find(y) > 0:
            #print(str_out.find(y), "%$%$%$^", x)
            print(y, x, file=ip_file)
            break
my_file.close()
ip_file.close()
