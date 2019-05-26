#-*-coding:utf-8-*-
#用递归法求5!的值(5的阶乘)
def Fact(n):
    if n == 1:
        fn=1
    else:
        fn = n*Fact(n-1)
    return fn
print(Fact(20))
