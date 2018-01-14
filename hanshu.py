def print_hanshu():
	
	sumj=0
	sumo=0
	zsum=0
	for i in range(0,101):
		
		if i%2 == 0:
			sumo = sumo+i
		elif i%2 !=0:
			sumj = sumj+i
		zsum =sumj+sumo
	print(zsum)
print_hanshu() 






