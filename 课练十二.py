#-*-coding:utf-8-*-
#输出第十个斐波那契数列
#斐波那契数列就是指黄金分割数列，指的是从数列第三项起每一项都等于前两项数之和，类似于兔子问题
a = int(input("输入要第几个数："))
a1,a2 = 1,1
for i in range(1,a+1):
    if (i <= 2):
        print("第%d个数为1" % i)
    else:
        if i == 3:
            a1 = a2
        else:
            a1,a2 = a2,a1+a2
        print("第%d个数为%d"%(i,(a1 + a2)))
