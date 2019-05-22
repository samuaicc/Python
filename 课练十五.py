#-*-coding:utf-8-*-
#输入一行字符，分别统计出其中英文字母，空格，数字和其他字符的个数
#要用到字符串的常用操作
s = input("请输入一行字符:")
#定义字母空格数字和其他字符的数量为0
letterNum = 0
spaceNum = 0
numberNum = 0
othersNum = 0
for c in s:
    if c.isalpha():
        letterNum += 1
    elif c.isspace():
        spaceNum += 1
    elif c.isdigit():
        numberNum += 1
    else:
        othersNum += 1
print("字母有%d个\n空格有%d个\n数字有%d个\n其他有%d个"%(letterNum,spaceNum,numberNum,othersNum))
