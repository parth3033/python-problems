print("Enter 'x' for exit.");
	print("Enter two numbers to find HCF and LCM: ");
	num1 = input();
	if num1 == 'x':
	    exit();
	else:
	    num2 = input();
	    number1 = int(num1);
	    number2 = int(num2);
	    temp1 = number1;
	    temp2 = number2;
	    while temp2 != 0:
	    	t = temp2;
	    	temp2 = temp1%temp2;
	    	temp1 = t;
	    hcf = temp1;
	    lcm = (number1*number2)/hcf;
	    print("HCF =",hcf);
	    print("LCM =",lcm);
