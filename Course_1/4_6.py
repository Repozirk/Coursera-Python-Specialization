def computepay(hrs,rate):
	if hrs<=40:
		pay=hrs*rate
	else:
		pay= (40*rate) + ((hrs-40)*1.5*rate)
	
	return pay

hrs_s = raw_input("Enter Hours:")
rate_s= raw_input("Enter Rate:")
hrs=float(hrs_s)
rate=float(rate_s)

p = computepay(hrs,rate)
print p