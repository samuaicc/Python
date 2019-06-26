#-*-coding:utf-8-*-
#有一个已经排好的数组。先输入一个数，要求按原来的规律将它插入数组中。
a = [1,3,9,11,20,25,48,59,88,100,0] #0作为占位符
print('原始数组:\n',a)
number = int(input('请输入一个数字：\n'))
end = a[9]
if number >= end:
    a[10] = number
else:
    for j in range(10):
        if a[j] > number:
            temp1 = a[j]
            a[j] = number
            for k in range(j + 1,11):
                temp2 = a[k]
                a[k] = temp1
                temp1 = temp2
            break
print('排序后列表:\n',a)

