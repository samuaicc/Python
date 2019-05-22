#-*-coding:utf-8-*-
#求s=a+aa+aaa+aaaa+aaaaa+.....的值，其中a是一个数字，相加的数字个数由用户输入决定
#解法:规律aa=a*(10)+a,aaa=a*(10**2)+a*10+a......
num = int(input("请输入要相加的数字(1-9):"))
time = int(input("请输入要相加的次数:"))
list = []
a = 0
for i in range(time):
    a += num * (10 ** i)   #aa=a*(10)+a,aaa=a*(10**2)+a*10+a......
    list.append(a)
#计算
print("s = ")
for j in range(len(list)):
    print(list[j],end='+')
print()
print("s =",sum(list))    #sum()函数求列表list的总和
    
    
