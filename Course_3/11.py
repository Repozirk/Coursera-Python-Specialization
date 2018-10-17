

name = raw_input("Enter file:")
if len(name) < 1 : name = "reg_sum_358859.txt"
handle = open(name)

all_num_list=list()
import re
for line in handle:
	all_num=re.findall('[0-9]+', line)
	#print len(all_num)
	if len(all_num) >0:
		all_num_list.append(all_num)
	else: continue
print all_num_list

int_num=list()
for num_str in all_num_list:
	if len(num_str)>1:
		for nums in num_str:
			num=int(nums)
			int_num.append(num)
	else:
		num=int(num_str[0])
		int_num.append(num)
	
print int_num

print sum(int_num)

