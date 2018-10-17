# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
s_num=0
num_count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
		#print line
		num_st=line.find(":")
		num_wsp=line[num_st+1:]
		num_raw=num_wsp.strip()
		num=float(num_raw)
		s_num=s_num+num
		num_count=num_count+1
		avg=s_num/num_count
print "Average spam confidence:",avg	
