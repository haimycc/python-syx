import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime
import xlrd
import xlwt


new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("updatesql.20170310.3", "a+") as f1:
        with open("updatesql.20170310.4", "a+") as f2:
            sql="select t.asset_id,t.phase from (select * from product.t_repayments r where r.properties=6 and actual_interest>0  order by phase asc) t group by t.asset_id "
            new_cursor.execute(sql)
            rows=new_cursor.fetchall()
            for row in rows:
                assetId=row["asset_id"]
                assetIdsuffix=int(str(assetId)[-2:])
                phase=row["phase"]
                f1.write("%s|%s\n" % (assetId,phase))
                updateSql="update product.t_repayment_%02d set properties=5 where asset_id=%d and phase=%d ;\n" % (assetIdsuffix,assetId,phase)
                updateSqls="update product.t_repayments set properties=5 where asset_id=%d and phase=%d ;\n" % (assetId,phase)
                f2.write(updateSql)
                f2.write(updateSqls)
handler()