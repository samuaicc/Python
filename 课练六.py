#-*-coding:utf-8-*-
#打印九九乘法表
#嵌套循环的使用
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2}'.format(i,j,(i*j)),end='\t')
    print() #换行
