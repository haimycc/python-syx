import datetime,calendar

#昨天的日期
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    return today-oneday

#明天的日期
def getTomorrow():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    return today+oneday

print(getYesterday())
print(getTomorrow())