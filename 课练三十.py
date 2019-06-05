#-*-coding:utf-8-*-
#输入一周内某一天的英文首字母判断这是星期几，第一个字母重复就判断第二个字母
f_letter = str(input('First letter:'))
if f_letter.upper() == 'M':
    print('This day is Monday !')
elif f_letter.upper() == 'W':
    print('This day is Wednesday !')
elif f_letter.upper() == 'F':
    print('This day is Friday !')
elif f_letter.upper() == 'S':
    sec_letter = str(input('Second letter:'))
    if sec_letter.lower() == 'a':
        print('This day is Saturday !')
    elif sec_letter.lower() == 'u':
        print('This day is Sunday !')
    else:
        print('Input Error!')
elif f_letter.upper() == 'T':
    sec_letter = str(input('Second letter:'))
    if sec_letter.lower() == 'u':
        print('This day is Tuesday !')
    elif sec_letter.lower() == 'h':
        print('This day is Thursday !')
    else:
        print('Input Error!')
else:
    print('Input Error!')
