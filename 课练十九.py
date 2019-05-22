#-*-coding:utf-8-*-
#一球从100米的高度自由落下，每次落地反弹至原高度的一半，在落下，那么它在第十次落地时，共经过多少米，第十次反弹多高
time = int(input('要求第几次:'))
high = 100.0
i = 1
list = []
while i < time+1:
    if i == 1:
        list.append(high)
    else:
        list.append(2*high)
    high /= 2
    i += 1
else:
    print('经过{0}米'.format(sum(list)))
    print('第{0}次反弹的高度为:{1}'.format(time,high))
'''
#使用for循环方法:
for i in range(1,time+1):
    if i == 1:
        list.append(high)
    else:
        list.append(2*high)
    high /= 2
print(sum(list))
print(high)
'''
