
import random 
computer=random.randint(1,100)
x=1
while x<=10 :
	y=int(input('请输入数字'))
	if y < computer:
		print("你猜测的结果偏小")
	if y > computer:
		print('你猜测的结果偏大')

	
	else:

		print('结果正确')
		break
	x+=1
