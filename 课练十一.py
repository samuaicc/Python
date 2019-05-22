#-*-coding:utf-8-*-
#对于一个正整数分解质因数
#把一个合数用质因数相乘的形式表达出来叫做分解质因数
a = int(input("请输入一个正整数:"))
num = a
list = []
while a != 1:
    for i in range(2,int(a+1)):
        if a % i == 0:
            list.append(str(i))
            a = a/i
        if a == 1:
            break
print(num,'=','*'.join(list))

