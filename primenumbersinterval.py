a=int(input('enter number'))
	count=0
	for i in range(2,a//2+1):
		if a%i==0:
			count+=1
			break
	
	if count==0 and a!=1:
		print('Number is prime',a)
	else:
		print('not prime',a)
