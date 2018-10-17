
import urllib
from BeautifulSoup import *

#function for extracting the names out of the url with regex
def name_extract(link):
	name_link=re.findall('([a-zA-Z]+)\.html', link)
	#print name_link[0] #monitoring print
	return name_link[0]

	
#first url form raw input, call function 'name_extract'
url = raw_input('Enter - ')
link=url
#print link #monitoring print
print name_extract(link)
	
# Looping x-times: get the links out of the url and extract the y link and name with help of 'name extract'
import re
num_of_loops=0
x=7
y=17
while num_of_loops<x:
	name_lst=list()
	link_lst=list()
	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	
	# retrieve all of the anchor tags
	tags = soup('a')
	
	for tag in tags:
		link=tag.get('href', None)
		link_lst.append(link)
		name_lst.append(name_extract(link))
	
	url=link_lst[y]
	#print url #monitoring print
	num_of_loops=num_of_loops+1
	print name_lst[y]
	


