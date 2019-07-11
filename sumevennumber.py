sum=0
	for i in range (1,31):
		if(i==10 or i==20):
			continue
		elif(i%2==0):
			sum=sum+i
	print(sum)
