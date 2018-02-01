import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

# 利息
def getInterest(map):
    date21 = datetime(2016, 11, 21)
    fullTime = map["full_time"]
    bidTime = map["bid_time"]
    phaseTotal = map["phase_total"]
    phaseMode = map["phase_mode"]
    isBefore21 = False
    sum = 0
    if fullTime <= date21:
        isBefore21 = True
    if isBefore21:
        sum += map["amount"] * map["annual_rate"] * 3 // 360
    else:
        newbidTime = datetime(bidTime.year, bidTime.month, bidTime.day)
        newfullTime = datetime(fullTime.year, fullTime.month, fullTime.day)
        diffDay = (newbidTime - newfullTime).days - 1
        if diffDay < 0:
            diffDay = 0
        sum += map["amount"] * map["annual_rate"] * diffDay // 360
    if phaseMode == 1:
        sum += map["amount"] * map["annual_rate"] * phaseTotal // 360
    elif phaseMode == 2:
        sum += map["amount"] * map["annual_rate"] * phaseTotal // 12
    elif phaseMode == 3:
        sum += map["amount"] * map["annual_rate"] * phaseTotal
    else:
        sum += 0
    sum = sum // 10000
    return sum


# 加息
def getAddInterest(map):
    date21 = datetime(2016, 11, 21)
    fullTime = map["full_time"]
    bidTime = map["bid_time"]
    phaseTotal = map["phase_total"]
    phaseMode = map["phase_mode"]
    isBefore21 = False
    sum = 0
    if fullTime <= date21:
        isBefore21 = True
    if isBefore21:
        sum += map["amount"] * map["add_rate"] * 3 // 360
    else:
        newbidTime = datetime(bidTime.year, bidTime.month, bidTime.day)
        newfullTime = datetime(fullTime.year, fullTime.month, fullTime.day)
        diffDay = (newbidTime - newfullTime).days - 1
        if diffDay < 0:
            diffDay = 0
        sum += map["amount"] * map["add_rate"] * diffDay // 360
    if phaseMode == 1:
        sum += map["amount"] * map["add_rate"] * phaseTotal // 360
    elif phaseMode == 2:
        sum += map["amount"] * map["add_rate"] * phaseTotal // 12
    elif phaseMode == 3:
        sum += map["amount"] * map["add_rate"] * phaseTotal
    else:
        sum += 0
    sum = sum // 10000
    return sum




num1=10000*800*6//360
num2=10000*800*1//12
num3=(num1+num2)//10000
print(num1)
print(num2)
print(num3)
