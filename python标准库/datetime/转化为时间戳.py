import datetime,calendar,time

#将字符串格式化成时间
d1=datetime.datetime.now()
d3=d1+datetime.timedelta(hours=10)
print(d3.ctime())

#将格式字符串转换为时间戳
t=time.mktime(time.strptime(d3.ctime(),"%a %b %d %H:%M:%S %Y"))
print(t)