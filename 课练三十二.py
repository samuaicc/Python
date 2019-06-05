#-*-coding:utf-8-*-
#按逗号分隔输出列表中的值
list = [1,2,3,4,5,6]
s = ','.join(str(x) for x in list)
print('按逗号分隔输出列表中的值:',s)
