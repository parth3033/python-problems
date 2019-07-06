a=int(input(''))
count=0
for i in  range(2,(a//2+1)):
	if a%i==0:
		count=count+1
		break
if count==0 and a!=1d:
	print('number is prime')
else:
	print('number is not prime')


