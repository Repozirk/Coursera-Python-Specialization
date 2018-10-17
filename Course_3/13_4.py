import json
import urllib

# retrieve the data source (JSON Date) with 'raw input'
address = raw_input('Enter - ')
    
url = urllib.urlopen(address)
data = url.read()
#print data #monitoring print
print 'Retrieved',len(data),'characters'


info = json.loads(data)
#print info #monitoring print
print 'User count:', len(info)

#search for the 'counts' in info and sum up the int
count_sum=0
for item in info['comments']:
	print 'Name', item['name']
	print 'count', item['count']
	count_sum =count_sum + int(item['count'])
print count_sum