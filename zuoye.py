#打星星
y=0
#x表示横 y表示列
while y < 10:
	x = 0
	while x < y:
		print('* ',end="")
		x +=1
	y +=1
	print('')
y=0
while y < 10:
	x=0
	while y < 10-x:
		print('* ',end="")
		x+=1
	y+=1
	print('')
