import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getErrorData():
    with open("./4updateSql.20170301","a+") as f:
        assetIdset=set()
        for idx in range(0,100):
            sql="select r.asset_id,r.repayment_id,r.phase " \
                "from " \
                "product.t_repayment_%02d r," \
                "(select * from (select * from product.t_repayment_%02d r where r.properties=6 order by phase asc) t group by t.asset_id ) s " \
                "where r.properties=6 " \
                "and r.asset_id=s.asset_id " \
                "and r.repayment_id<>s.repayment_id;" % (idx,idx)
            new_cursor.execute(sql)
            rows = new_cursor.fetchall()
            for row in rows:
                assetId=row["asset_id"]
                assetIdset.add(assetId)

        #遍历set
        for assetId in assetIdset:
            assetIdSuffix=int(str(assetId)[-2:])
            sql="select * from product.t_investment_%02d where asset_id = %d " % (assetIdSuffix,assetId)
            new_cursor.execute(sql)
            rows = new_cursor.fetchall()
            for row in rows:
                assetId=row["asset_id"]
                assetIdSuffix=int(str(assetId)[-2:])
                investId=row["investment_id"]
                investIdSuffix=int(str(investId)[-2:])
                financialId=row["financial_plan_id"]
                financialIdSuffix=int(str(financialId)[-2:])
                #找到这个投资记录的所有回款
                sql="select ifnull(sum(actual_principal),0) as actual_principal," \
                    "ifnull(sum(actual_interest),0) as actual_interest," \
                    "ifnull(sum(actual_add_interest),0) as actual_add_interest," \
                    "ifnull(sum(actual_pay_platform),0) as actual_pay_platform " \
                    "from invest.t_investment_payoff_%02d " \
                    "where " \
                    "asset_id = %d and " \
                    "investment_id = % d " % (investIdSuffix,assetId,investId)
                new_cursor.execute(sql)
                rows = new_cursor.fetchall()
                for row in rows:
                    actualPrincipal = row["actual_principal"]
                    actualInterest = row["actual_interest"]
                    actualAddInterest = row["actual_add_interest"]
                    actualPayPlatform = row["actual_pay_platform"]
                    updateSql1="update invest.t_investment_%02d " \
                               "set received_principal=%d," \
                               "received_interest=%d," \
                               "received_add_interest=%d," \
                               "actual_pay_platform=%d," \
                               "received_money=%d" \
                               " where " \
                               "asset_id = %d " \
                               "and investment_id = %d ;\n" % (investIdSuffix,actualPrincipal,actualInterest,actualAddInterest,actualPayPlatform,actualInterest+actualAddInterest,assetId,investId)
                    updateSql2="update product.t_investment_%02d " \
                               "set received_principal=%d," \
                               "received_interest=%d," \
                               "received_add_interest=%d," \
                               "actual_pay_platform=%d," \
                               "received_money=%d" \
                               " where " \
                               "asset_id = %d " \
                               "and investment_id = %d ;\n" % (assetIdSuffix,actualPrincipal,actualInterest,actualAddInterest,actualPayPlatform,actualInterest+actualAddInterest,assetId,investId)
                    updateSql3="update financial_plan.t_investment_%02d " \
                               "set received_principal=%d," \
                               "received_interest=%d," \
                               "received_add_interest=%d," \
                               "actual_pay_platform=%d," \
                               "received_money=%d" \
                               " where " \
                               "asset_id = %d " \
                               "and investment_id = %d ;\n" % (financialIdSuffix,actualPrincipal,actualInterest,actualAddInterest,actualPayPlatform,actualInterest+actualAddInterest,assetId,investId)
                    updateSqls="update invest.t_investments " \
                               "set received_principal=%d," \
                               "received_interest=%d," \
                               "received_add_interest=%d," \
                               "actual_pay_platform=%d," \
                               "received_money=%d" \
                               " where " \
                               "asset_id = %d " \
                               "and investment_id = %d ;\n" % (actualPrincipal,actualInterest,actualAddInterest,actualPayPlatform,actualInterest+actualAddInterest,assetId,investId)
                    f.write(updateSql1)
                    f.write(updateSql2)
                    f.write(updateSql3)
                    f.write(updateSqls)







getErrorData()