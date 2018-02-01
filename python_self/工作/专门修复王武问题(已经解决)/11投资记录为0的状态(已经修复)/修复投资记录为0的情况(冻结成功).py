import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


if __name__ == "__main__" :
    with open("./修复投资状态为0的情况(冻结成功).sql","a+") as f:
        for suffix in range(0,100):
            #找到投资表和投资流水表
            sql=str.format("select a.financial_plan_id,a.asset_id,a.asset_name,a.investment_id,a.investor_uid,a.create_time,a.amount,a.asset_type,asset_pool,b.operation from invest.t_investment_%02d a,invest.t_investment_flow_%02d b where a.investment_id=b.investment_id and a.state = 0 and b.operation= 3 and a.create_time <= '2017-01-09 00:00:00'" % (suffix,suffix))
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
                operation=list["operation"]
                assetType=list["asset_type"]
                assetPool=list["asset_pool"]
                sql1=str.format("update invest.t_investment_%02d set state = 3 where investment_id=%d and state = 0 ;\n" % (int(str(investId)[-2:]),investId))
                sql2=str.format("update product.t_investment_%02d set state = 3 where investment_id=%d and state = 0 ;\n" % (int(str(assetId)[-2:]),investId))
                sql3=str.format("update financial_plan.t_investment_%02d set state = 3 where investment_id=%d and state = 0 ;\n" % (int(str(financialId)[-2:]),investId))
                sqls=str.format("update invest.t_investments set state = 3 where investment_id=%d and state = 0 ;\n" % (investId))
                f.write(sql1)
                f.write(sql2)
                f.write(sql3)
                f.write(sqls)







