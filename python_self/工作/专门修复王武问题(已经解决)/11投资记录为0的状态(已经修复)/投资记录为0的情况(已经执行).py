import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    with open("./updateSql","a+") as f:
        sum=0
        for suffix in range(0,100):
            sql=str.format("select a.financial_plan_id,a.asset_id,a.investment_id,b.operation from invest.t_investment_%02d a,invest.t_investment_flow_%02d b where a.investment_id=b.investment_id and a.state = 0 and b.operation= 6 " % (suffix,suffix))
            new_cursor.execute(sql)
            lists = new_cursor.fetchall()
            for list in lists:
                financialId=list["financial_plan_id"]
                assetId=list["asset_id"]
                investId=list["investment_id"]
                operation=list["operation"]
                updateSql1=str.format("update product.t_investment_%s set state = 3 where asset_id = %d and investment_id = %d and state = 0 ;" % (str(assetId)[-2:],assetId,investId))
                updateSql2=str.format("update invest.t_investment_%s set state = 3 where asset_id = %d and investment_id = %d and state = 0 ;" % (str(investId)[-2:],assetId,investId))
                updateSql3=str.format("update financial_plan.t_investment_%s set state = 3 where asset_id = %d and investment_id = %d and state =0 ; " % (str(financialId)[-2:],assetId,investId))
                updateSqls=str.format("update invest.t_investments set state = 3 where asset_id = %d and investment_id = %d and state =0 ;" % (assetId,investId))
                f.write(updateSql1+"\n")
                f.write(updateSql2+"\n")
                f.write(updateSql3+"\n")
                f.write(updateSqls+"\n")
                checkSql=str.format("select asset_id,investment_id,operation from invest.t_investment_flow_%s where investment_id = %d and operation = 6 " % (str(investId)[-2:],investId))
                #print(checkSql)
                new_cursor.execute(checkSql)
                results = new_cursor.fetchall()
                if len(results) == 0 :
                    print(str.format("error:asset_id is %d,investment_id is %d" % (assetId,investId)))



