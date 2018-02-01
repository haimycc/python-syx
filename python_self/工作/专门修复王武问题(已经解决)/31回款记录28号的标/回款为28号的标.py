import os
import time
import mysql.connector
from datetime import *
from dateutil.relativedelta import *
import calendar

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("原28号回款的理财计划标的信息.csv", "a+") as f:
        f.write("标的ID,标的名字,募集金额,投资时间,募集期限,锁定期,修复后的退出期\n")
        two28Begin = datetime.strptime("2017-02-28 00:00:00", "%Y-%m-%d %H:%M:%S")
        two28End = datetime.strptime("2017-02-28 23:59:59", "%Y-%m-%d %H:%M:%S")

        sql="select * from product.t_assets where asset_type = 1 and asset_property & 65536 != 65536 "
        new_cursor.execute(sql)
        rows = new_cursor.fetchall()
        for row in rows:
            assetId=row["asset_id"]
            assetName=row["asset_name"]
            amount=row["total_amount"]
            investTime=row["invest_time"]
            bidTime=row["bid_time"]
            totalPhase=row["phase_total"]
            phaseMode=row["phase_mode"]
            finishTime=bidTime + relativedelta(months =+ totalPhase)
            exitTime=row["finish_time"]
            if two28Begin <= finishTime and finishTime <= two28End :
                f.write("%s,%s,%s,%s,%s月,%s,%s\n" % (assetId,assetName,amount,investTime,totalPhase,bidTime,exitTime))


handler()

