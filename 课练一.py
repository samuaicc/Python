#-*-coding:utf-8-*-
#输入四个不同的整数组合出不重复的三位数
a = int(input("输入第一个数:"))
b = int(input("输入第二个数:"))
c = int(input("输入第三个数:"))
d = int(input("输入第四个数:"))
allnum = (a,b,c,d)
time = 0
for x in allnum:
    for y in allnum:
        for z in allnum:
            if x != y and x != z and y != z:
                time += 1
                print(x,y,z)
                print('第%d种'%time)
                
                
            
