#-*-coding:utf-8-*-
#用条件运算符的嵌套完成：高于90分的成绩用a表示，60到89之间的用b表示，60分以下的用c表示
#条件运算符就是指三元运算符
x = input("请输入你的成绩:")
x = float(x)
grade = "A" if x >= 90 else "B" if 60<= x <= 89 else "C"  #注意else后面没有":"
print("你的成绩等级为:",grade)
