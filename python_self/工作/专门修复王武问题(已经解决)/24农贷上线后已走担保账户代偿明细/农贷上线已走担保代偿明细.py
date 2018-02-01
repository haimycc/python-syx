import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def genCSV():
    with open("农贷上线已走担保代偿明细.csv", "a+") as f:
        f.write("代偿日期,产品标题,还款ID,借款人姓名,借款人Mobile,代偿本金,代偿利息,代偿扣费费用,代偿机构\n")
        for idx in range(0,100):
            #代偿数据
            sql="select asset_id,repayment_id,phase,operation_role,operation,operation_name,create_time,principal,interest  from product.t_repayment_flow_%02d where operation_role = 2  and operation = 8 " \
                % (idx)
            new_cursor.execute(sql)
            rows = new_cursor.fetchall()
            for row in rows:

                #flow信息
                assetId=row["asset_id"]
                assetIdSuffix=int(str(assetId)[-2:])
                repayId=row["repayment_id"]
                repayIdSuffix=int(str(repayId)[-2:])
                phase=row["phase"]
                role=row["operation_role"]
                operation=row["operation"]
                operationName=row["operation_name"]
                createTime=row["create_time"]
                principal=row["principal"]
                interest=row["interest"]

                #Asset标的信息
                annualRate=0
                borrower=0
                sql="select * from product.t_assets where asset_id = %d " % (assetId)
                new_cursor.execute(sql)
                assets = new_cursor.fetchall()
                for asset in assets:
                    annualRate=asset["annual_rate"]
                    borrower=asset["borrower_uid"]
                    categoryType=asset["category_type"]
                    assetName=asset["asset_name"]
                    #农贷
                    if categoryType == 2 :
                        #查费用:
                        beginDate= createTime.strftime('%Y-%m-%d 00:00:00')
                        endDate=createTime.strftime('%Y-%m-%d 23:59:59')
                        sql="select * from product.t_assets_fee_%02d where asset_id = %d and operation = 2 and create_time <= '%s'  and create_time >= '%s'  " \
                            % (assetIdSuffix,assetId,endDate,beginDate)
                        new_cursor.execute(sql)
                        fees = new_cursor.fetchall()
                        amount=0
                        for fee in fees:
                            feeNode = fee ["fee_node"]
                            feeType = fee ["fee_type"]
                            feeAmount = fee ["fee_amount"]
                            amount = amount + feeAmount
                        #查mobile
                        mobile=0
                        sql="select mobile from user.t_user where id = %d " % borrower
                        new_cursor.execute(sql)
                        mobileRows = new_cursor.fetchall()
                        for mobileRow in mobileRows:
                            mobile=mobileRow["mobile"]
                        #查用户名
                        realName=""
                        sql="select * from user.t_user_detail where userid= %d " % (borrower)
                        new_cursor.execute(sql)
                        detailRows = new_cursor.fetchall()
                        for detailRow in detailRows:
                            realName=detailRow["real_name"]
                        #写数据
                        f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                                    (str(createTime),str(assetName),str(repayId),str(realName),str(mobile),str(principal),str(interest),str(amount),str(operationName)))


genCSV()






























