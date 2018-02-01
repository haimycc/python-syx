import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


if __name__ == "__main__" :
    with open("./修复终审失败情况(state=0).txt","a+") as f:
        sql="select asset_id  from asset.t_asset where state = 0  and create_time >= '2017-01-06 00:00:00' and create_time <= now()"
        new_cursor.execute(sql)
        lists = new_cursor.fetchall()
        for list in lists:
            assetId=list["asset_id"]
            sql=str.format("select * from  asset.t_asset_fee_%s where loan_id = %d and fee_node=3 and fee_standard = 0" % (str(assetId)[-2:],assetId))
            new_cursor.execute(sql)
            results = new_cursor.fetchall()
            for result in results:
                fee=result["fee_standard"]
                if fee == 0:
                    sql=str.format("update asset.t_asset_fee_%s set fee_state =1 where loan_id = %d and fee_node=3 ;\n" % (str(assetId)[-2:],assetId))
                    f.write(sql)