def caught_speeding(s,b):
		if b == True:
			if s<=65:
				return 0
			elif s>=66 and s<=85:
				return 1
			elif s>=86:	
				return 2
		elif b == False:
			if s<=60:
				return 0
			elif s>=61 and s<=80:
				return 1
			elif s>=81:	
				return 2
	print(caught_speeding(60,False))
	print(caught_speeding(65,False))
	print(caught_speeding(65,True))
	

