'''
#一到100奇数和与偶数和，总和
count = 0
osum = 0
jisum = 0
zsum = 0
while count <100:
	count+=1
	if count%2 == 0:
		osum=(count+osum)
		print('偶数和是%d'%osum)
	if count%2 !=2:
		jisum=(count+jisum)
		print('奇数和是%d'%jisum)
	zsum =count+zsum
print('奇数和偶数的和是%d'%zsum)
'''			




'''
#王者登录
sum1 = 0
myaccount = 123
mypasswd = 123
while sum1 < 3:
	account = int(input("请输入账号"))
	passwd = int(input("请输入密码"))
	if account==myaccount and passwd==mypasswd:
		print('登录成功')
		hero = int(input('请选择英雄\n0:鲁班 1:肉 3:法师'))
		if hero == 0:
			print('你选择了鲁班大师')
		if hero == 1:
			print('你选择了程咬金')
		if hero == 3:
			print('你选择了王昭君')
		else:
			break
	else:
		print('登录失败')
	sum1+=1
'''












#1-2+3-4+5等的和
count = 0
sum1 = 0
while  count <100:
	if count%2 == 0:
		 sum1=sum1 - count
	else:
		 sum1=sum1 + count
	count+=1
print('和是%d'%sum1)

		




