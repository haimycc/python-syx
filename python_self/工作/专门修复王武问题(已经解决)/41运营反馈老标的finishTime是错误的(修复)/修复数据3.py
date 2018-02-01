import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("updateSql.20170317.3","a+") as f:
        sql="select * from product.t_assets s where DATEDIFF(s.finish_time,s.publish_time)<30 and asset_type =0 and state = 10 "
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            assetId=row["asset_id"]
            assetTime=row["finish_time"]
            finishTime=""
            sql="select max(actual_date) as finishTime from product.t_repayments where asset_id = %d " % (assetId)
            new_cursor.execute(sql)
            repays = new_cursor.fetchall()
            for repay in repays:
                finishTime=repay["finishTime"]
            updateSql="update product.t_assets set finish_time = '%s' where asset_id = %d and state = 10  and asset_type = 0 and finish_time = '%s';\n" % (finishTime,assetId,assetTime)
            f.write(updateSql)

handler()
