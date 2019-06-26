#-*-coding:utf-8-*-
#对十个数进行排序
#可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
def paixu(*x):
    list = []
    for i in x:
        list.append(i)
        s = len(list)
        for a in range(s - 1):
            min = a
            for b in range(a + 1,s):
                if list[min] > list[b]:min = b
            list[a],list[min] = list[min],list[a]
    return list
if __name__ == '__main__':
    print(paixu(11,13,28,89,107,36,664,112,98,1))
        

