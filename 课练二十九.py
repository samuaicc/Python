#-*-coding:utf-8-*-
#判断一个五位数是不是回文数，如12321是回文数
def judge(x):
    a = x // 10000       #先分解数字
    b = x % 10000 // 1000   
    c = x % 1000 // 100
    d = x % 100 // 10
    e = x % 10
    if a == e and b == d:
        print('这是一个回文数!')
    else:
        print('这不是一个回文数!')
judge(15251)
