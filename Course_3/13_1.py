
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
print tags

import re
com_dict=dict()

for tag in tags:
    # Look at the parts of a tag and convert it to a string for regex, move it in a dict
	print 'TAG:',tag
	tag_str=str(tag)
	
	com_str=re.findall('[0-9]+', tag_str)
	com_str=str(com_str[0])
	com_dict[com_str]=com_dict.get(com_str,0)+1
	
print com_dict	

temp_sum=list()
temp_count=list()

# loop through the dict and sum up all the key,val
for key,val in com_dict.items():
	int_val=int(val)
	int_key=int(key)
	if int_val>1:
		int_key=int_key*int_val
	temp_count.append(int_val)
	temp_sum.append(int_key)

print sum(temp_count)
print sum(temp_sum)