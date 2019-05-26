#-*-coding:utf-8-*-
#求1+2!+3!+4!....20!+...的前n项和的值
n = int(input('要求前几项的和:'))
s = 0
a = 1
for i in range(1,n+1):
    a = a * i
    s = s + a 
print('前{0}项的和为:{1}'.format(n,s))


    
    
    
    
    
