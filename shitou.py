#石头剪刀布
import random
#自己
x = int(input('请输入石头1 剪刀2 布3'))
#电脑
y = random.randint(1,3)





if x <=3 and x >0:
	if (x==1 and y==3) or (x==2 and y==1) or(x==3 and y==2):
 		print("电脑赢")
	elif (y==1 and x==3) or (y==2 and x==1) or (y==3 and x==2):
		print("我赢")
	else:
		print('平局')
	if y==1:
		print('电脑石头')
	if y==2:
		print('电脑剪刀')
	if y==3:
		print('电脑布')
else:
	print('不合规则')	

