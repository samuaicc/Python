#-*-coding:utf-8-*-
#练习函数的使用
def pfc(a,b):
    s = (a + b) * (a - b)
    return s
def wqpf1(a,b):
    s = (a ** 2) + (2 * a * b) + (b ** 2)
    return s
def wqpf2(a,b):
    s = (a ** 2) - (2 * a * b) + (b ** 2)
    return s
def pjz(*num):
    p = sum(num) / len(num)
    return p
print(pfc(2,3))
print(wqpf1(2,3))
print(wqpf2(2,3))
print(pjz(1,2,3,4,5,6,7,8,9))

