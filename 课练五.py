#-*-coding:utf-8-*-
#输入三个整数x,y,z按照从小到大输出
list = []
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
list.append(x)
list.append(y)
list.append(z)
list.sort()
print(list)
