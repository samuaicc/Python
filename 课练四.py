#-*-coding:utf-8-*-
#输入年月日计算这一天为这一年的第几天
every = (0,31,28,31,30,31,30,31,31,30,31,30,31)
year = int(input('年:'))
month = int(input('月:'))
day = int(input('日:'))
if month not in range(1,13):
     raise ValueError("月份应该在一到十二之间！")
if month == 2:
    if day > 29:
        raise ValueError ("二月不得超过二十九天！")
if year % 400 != 0 or year % 4 != 0 and year % 100 == 0:
    if month == 2:
        if day >= 29:
             raise ValueError("平年二月没有二十九天！")
if month in (4,6,9,11):
    if day > 30:
         raise ValueError("这些月份没有三十一天！")
if day not in range(1,32):
     raise ValueError("天数不能超过三十一天！")

if year % 400 != 0 or year % 4 != 0 and year % 100 == 0:
    alday = 0
    
    alday = sum(every[:month])
    
    alday += day
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    if month > 2:
        alday += 1
print("*"*30)
print("这是今年的第%d天"%alday)
