#-*-coding:utf-8-*-
#暂停一秒输出并格式化当前时间
#使用到了时间模块和函数
import time     #引入时间模块
time.sleep(1)   #暂停一秒输出
localtime = time.time()     #获取当前时间戳，此句不影响后面输出，可要可不要
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))   #格式化当前时间     
