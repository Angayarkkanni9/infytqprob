def generate_dict(number):
	l1=[]
	l2=[]
	for i in range(1,number+1):
	    l1.append(i)
	for i in range(1,number+1):
	    l2.append(i**2)
	dic=dict(zip(l1,l2))
	
	return str(dic)

number=10
print(generate_dict(number))
