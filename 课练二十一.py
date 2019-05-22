#-*-coding:utf-8-*-
'''
两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，
请编程序找出三队赛手的名单。
'''
'''
需要用到ord()函数，
ord()函数是chr()函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
它以一个字符（长度为1的字符串）作为参数，
返回对应的 ASCII 数值，或者 Unicode 数值，
如果所给的 Unicode 字符超出了你的 Python 定义范围，
则会引发一个 TypeError 的异常
'''
for a in range(ord('x'),ord('z')+1):
    for b in range(ord('x'),ord('z')+1):
        for c in range(ord('x'),ord('z')+1):
            if a != b and a != c and b != c:
                if a != ord('x') and c != ord('x') and c != ord('z'):
                    print('对战名单为:\n a vs %s\n b vs %s\n c vs %s'%(chr(a),chr(b),chr(c)))
