#-*-coding:utf-8-*-
#求b到c之间有几个素数，分别为多少？
#素数是指只能被1和自身整除的数
a = int(input("开始数:"))
b = int(input("结束数:"))
list = []
for num in range(a,b+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        if num != 0 and num != 1:
            list.append(num)
print("素数为:",list)
print("一共有%d个素数"%len(list))
       
                
        
            
        
         
