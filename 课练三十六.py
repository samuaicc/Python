#-*-coding:utf-8-*-
#求3*3一个矩阵的主对角线元素之和
#矩阵的主对角线元素是指从左上角到右下角的所有元素
#矩阵通过使用嵌套列表表示    例如： [[1,2,3],[4,5,6],[7,8,9]]
#每个字列表中的元素是每一行中的元素，列表的个数就是矩阵的列数
sum = 0.0
l = []
for i in range(3):
    l.append([])
    for j in range(3):
        l[i].append(float(input('输入数字到矩阵:')))
for b in range(3):
    sum += l[b][b]
print('矩阵的主对角线元素之和为:',sum)
