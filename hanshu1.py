
name = input('请输入名字')
age = input('请输入年龄')
list=[{'name':name,'age':age}]
for i in list:
	for y in i:	
		print(y,i[y])	
