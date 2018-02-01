import os
import datetime, time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


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


def updateFinishTime():
    with open(os.path.abspath(os.curdir) + '/updateFinishTime', 'a+') as f:
        sql = "select * from product.t_assets where asset_type = 1 and asset_property & 65536 != 65536 and finish_time = '0000-00-00 00:00:00' and state in (5,6,7,8) ;"
        new_cursor.execute(sql)
        results = new_cursor.fetchall()
        for result in results:
            assetId = result["asset_id"]
            assetIdSuffix = str(assetId)[-2:]
            bidTime = result["bid_time"]
            phaseTotal = result["phase_total"]
            phaseMode = result["phase_mode"]
            map = {
                "bid_time": bidTime,
                "phase_total": phaseTotal,
                "phase_mode": phaseMode
            }
            finishTime = getExpectDate(map)

            # print("bidtime=%s,phaseMode=%d,phaseTotal=%d,finishTime=%s" % (bidTime,phaseMode,phaseTotal,finishTime))
            assetSql = str.format(
                "update product.t_assets set finish_time='%s' where asset_id=%d and finish_time='0000-00-00 00:00:00';" % (
                finishTime, assetId))
            f.write(assetSql + "\n")
            # 更新所有投资记录表
            investSql = str.format(
                "select investment_id from product.t_investment_%s where asset_id=%d" % (assetIdSuffix, assetId))
            new_cursor.execute(investSql)
            invests = new_cursor.fetchall()
            for invest in invests:
                investId = invest["investment_id"]
                investIdSuffix = str(investId)[-2:]
                sql1 = str.format(
                    "update invest.t_investment_%s set finish_time = '%s' where asset_id = %d and investment_id = %d and finish_time='0000-00-00 00:00:00'; " % (
                    investIdSuffix, finishTime, assetId, investId))
                sql2 = str.format(
                    "update product.t_investment_%s set finish_time = '%s' where asset_id = %d and investment_id = %d and finish_time='0000-00-00 00:00:00';" % (
                    assetIdSuffix, finishTime, assetId, investId))
                sql3 = str.format(
                    "update financial_plan.t_investment_%s set finish_time = '%s' where asset_id = %d and investment_id= %d and finish_time='0000-00-00 00:00:00';" % (
                    assetIdSuffix, finishTime, assetId, investId))
                sqls = str.format(
                    "update invest.t_investments set finish_time= '%s' where asset_id = %d and investment_id = %d and finish_time='0000-00-00 00:00:00';" % (
                    finishTime, assetId, investId))
                print(sql1)
                print(sql2)
                print(sql3)
                print(sqls)
                f.write(sql1 + "\n")
                f.write(sql2 + "\n")
                f.write(sql3 + "\n")
                f.write(sqls + "\n")


if __name__ == "__main__":
    updateFinishTime()
