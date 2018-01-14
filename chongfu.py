def print_chongfu:
	list=[]
	while True:
		zidian = {}
		name = input('请输入名字')
		age = input('请输入年龄')
		soft=[]
		for i in list:
			for k,v in i.items():
				soft.append(v)
		a=soft.count(name)
		if a==0:
			zidian['name']=name
			zidian['age']=age
			list.append(zidian)
		else:
			print('重复，重新输入')
		print(list)
		for i in list:
			for k,v in i.items():
				print(k,v)
print_chongfu()

