#coding=utf-8

import time


print time.time()  #输出时间戳

print "2017-07-07 18:33:59" > ""

struct = time.localtime(time.time()) #返回结构体 time.struct_time(tm_year=2010, tm_mon=7, tm_mday=19, tm_hour=22, tm_min=33, tm_sec=39, tm_wday=0, tm_yday=200, tm_isdst=0)

print struct

currentTime = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print currentTime

print "2017-07-07 18:28:59" > "2017-07-07 18:29:58"

while True:
    currentTime = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print currentTime
    success = currentTime < "2017-07-07 18:33:59"
    print success
    if success :
        continue
    else :
        break
