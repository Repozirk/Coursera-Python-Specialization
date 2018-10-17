largest = None
smallest = None
while True:

	num = raw_input("Enter a number: ")
	if num == "done":
		#print num
		break
	else:
		try:
			inum=int(num)
		except:
			print "Invalid input"
			continue

	#print num
	
	if largest is None:
		largest=num
	elif largest<num:
		largest=num
		
	if smallest is None:
		smallest=num
	elif smallest>num:
		smallest=num	

print "Maximum is", largest
print "Minium is", smallest

