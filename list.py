#列表
midncv='欢迎进入个人信息表'
print(midncv.center(40,'*'))
list1=[]
while True:
	
	
	mode = int(input('请选择功能 1.添加  2.查询 3.修改 4.删除'))
	if mode == 1:
		name = input('请输入名字')
		age = input('请输入年龄')
		sex = input('请输入性别') 
		work = input('请输入工作')
		

		list1.append(name)
		list1.append(age)
		list1.append(sex)
		list1.append(work)
		print(list1)
	elif mode == 2:
		suoyin=int(input('请输入索引'))
		print(list1[suoyin])
	elif mode == 3:
		name1=input('请输入名字'))
		newname=input('请输入新的名字'))
		list1[0]=newname
		print(list1)
	elif mode == 4:
		delname = input('请输入要删除的名字')
		list1.remove(delname) 
		print(list1)
