#-*-coding:utf-8-*-
#第五个人岁数问题
def age(a):
    b = 10
    for i in range(1,a):
        b += 2
    return b
print('第五个人的岁数为:',age(5))
