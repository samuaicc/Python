#-*-coding:utf-8-*-
#输出一百以内的素数
def sushu(x,y):
    list = []
    for i in range(x,y + 1):
        for a in range(2,i):
            if i % a == 0:
                break
        else:
            if i != 0 and i != 1:
                list.append(i)
    return list
if __name__ == '__main__':
    print(sushu(100,1000))
