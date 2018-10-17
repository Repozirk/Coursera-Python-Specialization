name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=0
all_senders=list()
senders=dict()

##split the lines and store the words in a list
##fill the dictionary with the words in the list with help of  "get"
for line in handle:
    if not line.startswith("From ") : continue
    else:
		words=line.split()
		all_senders.append(words[1])
		
for email in all_senders:
	senders[email]=senders.get(email,0)+1
#print all_senders		
#print senders

##Search for the most frequent email adress
freq_email=None
frequency= None
for email,count in senders.items():
	if frequency is None or count> frequency:
		freq_email=email
		frequency=count

print freq_email, frequency