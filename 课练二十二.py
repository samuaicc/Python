#-*-coding:utf-8-*-
#输出菱形图案
from sys import stdout
g = int(input('输入一个单数控制层数:'))
e = int((g-1)/2)
for i in range(e+1):
    for j in range(e - i):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print()
for a in range(e):
    for b in range(a + 1):
        stdout.write(' ')
    for c in range((g - 2) - a * 2):
        stdout.write('*')
    print()
