def leap(a):
	if a%4 == 0 and a%100 != 0 and a%400 == 0:
		print("闰年")
	else:
		print("平年")
a = int(input("请输入年份"))
leap (a)

