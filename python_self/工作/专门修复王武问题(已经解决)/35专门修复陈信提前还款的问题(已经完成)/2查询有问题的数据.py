import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getErrorData():
    with open("./2updateSql.20170301.1","a+") as f:
        for idx in range(0,100):
            sql="select r.asset_id,r.repayment_id,r.phase from product.t_repayment_%02d r,(select * from (select * from product.t_repayment_%02d r where r.properties=6 order by phase asc) t group by t.asset_id ) s where r.properties=6 and r.asset_id=s.asset_id and r.repayment_id<>s.repayment_id;" % (idx,idx)
            new_cursor.execute(sql)
            rows = new_cursor.fetchall()
            for row in rows:
                assetId=row["asset_id"]
                repayId=row["repayment_id"]
                phase=row["phase"]
                updateSql="update product.t_repayment_%02d set actual_interest=0,actual_pay_guarantee=0,actual_pay_incoming=0,actual_pay_platform=0,actual_pay_fee=0 where asset_id=%d and repayment_id=%d and phase=%d ;\n" % (idx,assetId,repayId,phase)
                updateSqls="update product.t_repayments set actual_interest=0,actual_pay_guarantee=0,actual_pay_incoming=0,actual_pay_platform=0,actual_pay_fee=0 where asset_id=%d and repayment_id=%d and phase=%d ;\n" % (assetId,repayId,phase)
                f.write(updateSql)
                f.write(updateSqls)


getErrorData()