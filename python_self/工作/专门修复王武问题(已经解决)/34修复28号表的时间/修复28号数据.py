import os
import time
import mysql.connector
from datetime import *
from dateutil.relativedelta import *
import calendar

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("updateSql.20170301", "a+") as f:
        assetIdLists=[
            20170122000017603,
            20170122000031203,
            20170122000032003,
            20170122000057303,
            20170122000092103,
            20170122000093203,
            20170123000019103,
            20170123000019503,
            20170123000038503,
            20170123000050503,
            20170123000061003,
            20170123000071503,
            20170123000080903,
            20170123000118403,
            20170123000118803,
            20170124000004203,
            20170124000013703,
            20170124000015103,
            20170124000022003,
            20170124000022803,
            20170124000025703,
            20170124000026203,
            20170124000027203
        ]
        for assetId in assetIdLists:
            sql="select finish_time from product.t_assets where asset_id = %d and state = 10 " % (assetId)
            new_cursor.execute(sql)
            rows=new_cursor.fetchall()
            for row in rows:
                finishTime=row["finish_time"]
                updateSql="update specialDB.t_new_financial_plan_payoff set expect_date = '%s' where asset_id = %d and state = 3 ;\n" % (finishTime,assetId)
                f.write(updateSql)

handler()