#-*-coding:utf-8-*-
#一个整数加上a后是一个完全平方数，加上b后是一个完全平方数，这个数为多少？
import math
a = int(input("输入a:"))
b = int(input("输入b:"))
for i in range(10000):
    x = int(math.sqrt(i + a))
    y = int(math.sqrt(i + b))
    if x * x == i + a and y * y == i + b:
        print("这个数字是:%d"%i)
