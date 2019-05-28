#-*-coding:utf-8-*-
#给一个不多于五位的正整数，要求：1，求它是几位数2，逆序显示各位数字
def num(int1):
    a = str(int1)
    b = len(a)
    print('这是一个{0}位数'.format(b))
    if b == 0:
        return
    else:
        for i in range(1,b+1):
            print(a[-i])
num(2362135)            
#第二种方法    
x = int(input("请输入一个数:\n"))
a = x // 10000       #先分解数字
b = x % 10000 // 1000   
c = x % 1000 // 100
d = x % 100 // 10
e = x % 10
 
if a != 0:
    print ("5 位数：",e,d,c,b,a)
elif b != 0:
    print ("4 位数：",e,d,c,b)
elif c != 0:
    print ("3 位数：",e,d,c)
elif d != 0:
    print ("2 位数：",e,d)
else:
    print ("1 位数：",e)
