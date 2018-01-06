'''
age = int(input("请输入一个年龄"))

if age < 18 :
	print("不准谈恋爱")
elif age == 20:
	print("抓紧谈对象")
elif age > 30:
	print("完了，单身狗")
elif age == 18:
	print("恭喜你成年了")
else:
	print("sorry,系统出错")
'''





'''
num = 0
while num<4:
	site = input("请输入一个位置")
	if site == "ABC":
		print("后裔，黄忠，虞姬")
	elif site == "肉盾":
		print("亚瑟，程咬金")
	elif site == "法师":
		print("王昭君，妲己")
	elif site == "刺客":
		print("兰陵王，荆轲")
	num+=1
'''





















'''
hight = int(input("请输入身高"))
shenjia = int(input("请输入身价"))
yanzhi = int(input("请输入颜值"))
if hight > 180 and shenjia > 1000000 and yanzhi > 90:
	print("你就是高富帅")
elif hight < 180 and shenjia > 1000000 and yanzhi > 90:
	print("就可以算富帅")
elif hight < 180 and shenjia < 1000000 and yanzhi > 90:
	print("就可以是帅")
elif hight < 180 and shenjia < 1000000 and yanzhi < 90:
	print("就是矮矬穷")
else:
	print("就是一个屌丝")
'''





'''
year = int(input("请输入年份"))
if year%4==0 and not(year%100==0) or year%400==0:
	print("这是闰年")
else:
	print("那就是平年")
'''

'''
x = int(input("输入x:"))
y = int(input("输入y:"))
a = input("输入（+ - * / **）")
if a=="+":
	print("x+y=",x+y)
elif a=="-":
	print("x-y=",x-y)
elif a=="*":
	print("x*y=",x*y)
elif a=="/":
	print("x/y=",x/y)
elif a=="**":
	print("x**y=",x**y)
'''



'''
height = float(input("请输入身高"))
weight = float(input("请输入体重"))
BIM = weight/(height**2)
if BIM < 18.5:
	print("过轻")
elif BIM > 18.5 < 25:
	print("正常")
elif BIM > 25 < 28:
	print("过胖")
elif BIM > 28 < 32:
	print("肥胖")
elif BIM > 32:
	print("严重肥胖")
'''



myaccount =int(input("请输入一个账号")
mypasswd = int(input('请输入密码')
if myaccount==accound and mypasswd==passwd:
	print("登录成功")
elif myaccouunt!=accound
	print("账号不对")
elif mypasswd!=passwd:
	print("密码不对")


