
def user_input():
		year =int(input('请输入年份'))
		month = int(input('请输入月份'))
		day = int(input('请输入日期'))
		count_day(year,month,day)

def count_day(year,month,lday):
		day =0
		dam =[1,3,5,7,8,10,12]
		xm =[4,6,9,11]
		for i in range(1,month):
			if i in dam:
				day=+31
			if i in xm:
				day=+30
			else:
				if rn_year:
					day+=29
				else:
					day+=28
		lday+=day 
		print('%d'%lday)


def rn_year(): 
		if (year%4 ==0 and year%100 ==0) or year%400!=0:
			return 1
		else:
			return 0
	
user_input



