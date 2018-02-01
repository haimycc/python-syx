import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("updateSql.20170317.2","a+") as f:
        sql="SELECT a.asset_id,a.finish_time as finishtime1,b.finish_time as finishtime2 FROM product.t_assets a,(SELECT asset_id,max(actual_date) AS finish_time  FROM product.t_repayments  GROUP BY asset_id ORDER BY actual_date ) b WHERE a.asset_id = b.asset_id AND a.state = 10 AND DATE(a.finish_time) < DATE(b.finish_time)   "
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            assetId=row["asset_id"]
            aFinishTime=row["finishtime1"]
            if aFinishTime == None or aFinishTime == "0000-00-00 00:00:00":
                aFinishTime = "0000-00-00 00:00:00"
            bFinishtime=row["finishtime2"]
            updateSql="update product.t_assets set finish_time = '%s' where asset_id = %d and finish_time = '%s' and state = 10 ;\n" % (bFinishtime,assetId,aFinishTime)
            f.write(updateSql)

handler()



