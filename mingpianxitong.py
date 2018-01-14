str = "名片系统"
print(str.center(40,"*"))



list_user =[]
def add_user():
	
	
	name = input('请输入名字')
	age =input('请输入年龄')
	sex =input('请输入性别')
	work =input('请输入工作')
	address =input('请输入地址')
	diant={'name':name,'age':age,'sex':sex,'work':work,'address':address}	
	list_user.append(diant)
	for i in list_user:
		print(i)
add_user()		
def xiugai_user():

	yuanlai = input('请输入修改前的内容')
	houlai =input('请输入修改后的内容')
	for i in list_user:
		for k,v in i.items():
			if v == yuanlai :
				i[k]=houlai
				break
		print(i)	
xiugai_user()				 



def shanchu_user():
	

	kill=input('请输入删除的内容')
	for i in list_user:
		for k,v in i.items():
			if kill == v:
				a=list_user.count(i)
				list_user.pop(a)
				break
		print(i)

				


		

			
	
	
		
			
	



		 
		
			
			
				
			
			

