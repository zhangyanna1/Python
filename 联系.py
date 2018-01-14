



def kill():
	print('杀人')




def play():
	print("开始捡东西")
	kill()



def denglu(token):
	if token == 123:
		print('登陆成功')
		play()
	else:
		print('登录失败')
	  






def saoyisao():
	print('开始扫一扫')
	denglu(123)

	

saoyisao()







