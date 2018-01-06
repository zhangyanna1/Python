#银行取钱
account = 1234567
passwd = 123123
money = 200000
myaccount = int(input("请输入账号"))
mypasswd = int(input("请输入密码"))

if myaccount == account and mypasswd == passwd:
	print("登录成功")
	mode = int(input("请输入模式 1存 2取：")) 
	if mode == 2:
		mymoney=int(input("请输入取款金额"))
		if mymoney >money:
			print("余额不足")
		elif mymoney <=money:
			print("取款%d元，剩余%d元"%(mymoney,money-mymoney))
else:
	print("账号错误")
'''































