#-*-coding:utf-8-*-
#输出所有"水仙花数"
#水仙花数是指一个三位数，其各位数字立方和等于该数本身
list = []
for i in range(100,1000):
    i = str(i)
    a,b,c = i[0],i[1],i[2]
    a = int(a)
    b = int(b)
    c = int(c)
    i = int(i)
    if (i == a ** 3 + b ** 3 + c ** 3):
        list.append(i)
print(list)
print("水仙花数一共有%d个"%len(list))

