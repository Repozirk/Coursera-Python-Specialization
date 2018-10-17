score = raw_input("Enter Score: ")
try:
	fl_score=float(score)
except:
	print "Sorry, Score must be a number!"
	quit()
	
if fl_score>1.0:
	print "Sorry, Score is out of range!"
	quit()
elif fl_score<0.0:
	print "Sorry, Score is out of range!"
	quit()
elif fl_score>=0.9:
	print "A"
elif fl_score>=0.8:
	print "B"
elif fl_score>=0.7:
	print "C"
elif fl_score>=0.6:
	print "D"
elif fl_score<0.6:
	print "F"
	

	