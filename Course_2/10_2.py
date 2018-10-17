name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

## create empty dictionary
hh_dict=dict()

## split hhmmss out of the line 
for line in handle:
    if not line.startswith("From ") : continue
    else:
		words=line.split()
		time= words[5]
		hhmmss=time.split(':')
		hh=str(hhmmss[0])
						
		#print time
		#print hh
		
		##shifting the hh as key into a dictionary with the frequency as val
		hh_dict[hh]=hh_dict.get(hh,0)+1
		#print hh_dict

## create list		
temp=list()
## create a tuple with the key,val and sort it by the key
for key,val in hh_dict.items():
	temp.append((key,val))
	temp.sort()
##	print the sorted key and val for all items in temp
for key, val in temp[:]:
	print key, val