import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145', user='search', password='search@zyxr.com', database='invest')
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


# 预计日期
def getExpectDate(map):
    bidTime = map["bid_time"]
    phaseTotal = map["phase_total"]
    phaseMode = map["phase_mode"]
    finishTime = None
    if phaseMode == 1:
        finishTime = bidTime + dateutil.relativedelta.relativedelta(days=+phaseTotal)
    elif phaseMode == 2:
        finishTime = bidTime + dateutil.relativedelta.relativedelta(months=+phaseTotal)
    elif phaseMode == 3:
        finishTime = bidTime + dateutil.relativedelta.relativedelta(years=+phaseTotal)
    return finishTime


def updateExpect():
    with open(os.path.abspath(os.curdir) + '/updateExpect', 'a+') as f:
        sql = "select * from product.t_assets where asset_id= 20161104000009912;"
        new_cursor.execute(sql)
        results = new_cursor.fetchall()
        for result in results:
            assetId = result["asset_id"]
            assetIdSuffix = str(assetId)[-2:]
            # 更新所有投资记录表
            investSql = str.format(
                "select investment_id,amount from product.t_investment_%s where asset_id=%d" % (assetIdSuffix, assetId))
            new_cursor.execute(investSql)
            invests = new_cursor.fetchall()
            for invest in invests:
                investId = invest["investment_id"]
                investIdSuffix = str(investId)[-2:]
                map = {
                    "asset_id": assetId,
                    "investment_id": investId,
                    "annual_rate": result["annual_rate"],
                    "add_rate": result["add_rate"],
                    "full_time": result["full_time"],
                    "bid_time": result["bid_time"],
                    "phase_total": result["phase_total"],
                    "phase_mode": result["phase_mode"],
                    "amount": invest["amount"]
                }
                # 预计利息
                expectInterest = getInterest(map)
                expectAddInterest = getAddInterest(map)
                expectDate = getExpectDate(map)
                print(
                    "asset id is " + str(assetId) + ",investment_id is " + str(investId) + ",expectInterest is " + str(
                        expectInterest) + ",expectAddInterest is " + str(expectAddInterest) + ",expectDate is " + str(
                        expectDate))


if __name__ == "__main__":
    updateExpect()
