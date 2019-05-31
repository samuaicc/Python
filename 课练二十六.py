#-*-coding:utf-8-*-
#利用递归函数调用方法将所输入的五个字符以相反顺序输出
def output(s,l):
    if l==0:
       return
    else:
       print (s[l-1])
       output(s,l-1)
s = input('Input a string:')
l = len(s)
output(s,l)
    
