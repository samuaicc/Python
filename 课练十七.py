#-*-coding:utf-8-*-
#一个数如果恰好等于它的因子数之和，那么这个数被称为完数，请输入num以前的全部完数
#应该先判断是否为素数，然后进行因数分解，然后判断因数之和是否为这个数
max = int(input("请输入范围:"))
for n in range(1,max):
    list = []
    for a in range(1,n):
        if n%a == 0:
            list.append(a)
    if sum(list) == n:
        print(n)

        

    
