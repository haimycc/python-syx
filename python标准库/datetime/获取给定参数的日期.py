import datetime,calendar

def GetDaysByNum(num):
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    li=[]
    for i in range(0,num):
        today=today-oneday
        li.append(str(today))
    return li

print(str(GetDaysByNum(4)))