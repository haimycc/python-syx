import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


if __name__ == "__main__" :
    with open("./修复投资状态为0的情况(未知成功或者失败).sql","a+") as f:
        for suffix in range(0,100):
            #找到投资表
            sql=str.format("select financial_plan_id,asset_id,asset_name,investment_id,investor_uid,create_time,amount,asset_type,asset_pool from invest.t_investment_%02d where state = 0 and create_time <='2017-01-09 00:00:00'" % (suffix))
            new_cursor.execute(sql)
            lists = new_cursor.fetchall()
            for list in lists:
                financialId=list["financial_plan_id"]
                assetId=list["asset_id"]
                assetName=list["asset_name"]
                investId=list["investment_id"]
                investorUid=list["investor_uid"]
                createTime=list["create_time"]
                amount=list["amount"]
                assetType=list["asset_type"]
                assetPool=list["asset_pool"]
                #是否有明确成功或者失败的流水
                sql=str.format("select operation from invest.t_investment_flow_%s where investment_id=%d and operation in (3,4)" % (str(investId)[-2:],investId))
                new_cursor.execute(sql)
                results = new_cursor.fetchall()
                #如果没有明确成功或者失败,就是未知是否有冻结
                if len(results) ==  0:
                    sql1=str.format("update invest.t_investment_%02d set state = 3 where investment_id = %d and state = 0 ;\n" % (int(str(investId)[-2:]),investId))
                    sql2=str.format("update product.t_investment_%02d set state = 3 where investment_id = %d and state = 0 ;\n" % (int(str(assetId)[-2:]),investId))
                    sql3=str.format("update financial_plan.t_investment_%02d set state = 3 where investment_id= %d and state = 0 ;\n" % (int(str(financialId)[-2:]),investId))
                    sqls=str.format("update invest.t_investments set state =3 where investment_id = %d and state = 0 ;\n" % (investId))
                    f.write(sql1)
                    f.write(sql2)
                    f.write(sql3)
                    f.write(sqls)







