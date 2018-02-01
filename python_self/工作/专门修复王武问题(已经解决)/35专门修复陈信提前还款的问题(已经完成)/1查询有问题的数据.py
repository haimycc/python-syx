import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getErrorData():
    with open("./1updateSql.20170301.1","a+") as f:
        for idx in range(0,100):
            sql="select asset_id,repayment_id,expect_date,actual_date from product.t_repayment_%02d " \
                "where " \
                "date(expect_date) = date(actual_date) and properties= 5 " % (idx)
            new_cursor.execute(sql)
            rows = new_cursor.fetchall()
            for row in rows:
                assetId=row["asset_id"]
                repayId=row["repayment_id"]
                expectDate=row["expect_date"]
                actualDate=row["actual_date"]
                updateSql="update product.t_repayment_%02d set properties=0 where asset_id=%d and repayment_id=%d and date(expect_date)=date(actual_date)  and properties=5 ;\n " % (idx,assetId,repayId)
                updateSqls="update product.t_repayments set properties=0 where asset_id=%d and repayment_id=%d and date(expect_date)=date(actual_date) and properties=5 ;\n " % (assetId,repayId)
                f.write(updateSql)
                f.write(updateSqls)


getErrorData()




