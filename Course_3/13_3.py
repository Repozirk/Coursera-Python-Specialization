import urllib
import xml.etree.ElementTree as ET

# retrieve the data source (xml-file) with 'raw input'
address = raw_input('Enter - ')
    
url = urllib.urlopen(address)
data = url.read()
#print data #monitoring print
print 'Retrieved',len(data),'characters'

#handle the xml into 'tree' structure of python
tree = ET.fromstring(data)

#create a list of all the 'comments' data
lst=tree.findall('.//comment')
print len(lst)
#print lst #monitoring print

sum_counts=0

#looping the items of the list and extrxt the 'count' data; sum it up and print it
for item in lst:
	c = item.find('count').text
	sum_counts=sum_counts+int(c)
	#print 'Count:' ,c #monitoring print

print sum_counts
