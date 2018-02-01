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
    with open("代偿方给代偿方费用.csv", "a+") as f:
        f.write("标的名称,标的ID,还款ID,还款第几期,代偿方,费用接收方,金额(分),角色,日期\n")
        #找到所有代偿过的线上还款记录
        for idx in range(0,100):
            sql="select * from product.t_assets_fee_%02d where fee_suid=fee_duid and operation = 2 group by repayment_id,asset_id" % (idx)
            new_cursor.execute(sql)
            rows=new_cursor.fetchall()
            for row in rows:
                assetId=row["asset_id"]
                repayId=row["repayment_id"]
                suid=row["fee_suid"]
                phase=row["phase"]
                createTime=row["create_time"]
                amount=row["fee_amount"]
                role=row["fee_drole"]
                if role == 1 :
                    role="用户"
                elif role == 2 :
                    role="担保商"
                elif role == 3 :
                    role="进件方"
                elif role == 4 :
                    role="平台"
                #标的信息
                assetName=""
                sql="select * from product.t_assets where asset_id = %d " % (assetId)
                new_cursor.execute(sql)
                assetRows=new_cursor.fetchall()
                for assetRow in assetRows:
                    assetname=assetRow["asset_name"]
                #代偿方信息
                userName=""
                sql="select * from user.t_user_detail where userid= %d" % (suid)
                new_cursor.execute(sql)
                userRows=new_cursor.fetchall()
                for user in userRows:
                    userName=user["real_name"]
                #还款信息
                f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (str(assetname),str(assetId),str(repayId),str(phase),userName,userName,str(amount),role,createTime))



handler()