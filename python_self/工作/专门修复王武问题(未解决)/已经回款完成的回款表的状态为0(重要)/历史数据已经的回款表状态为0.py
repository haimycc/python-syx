import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def genSql():
    with open("updatesql.20170224","a+") as f:
        sql="select * from invest.t_investment_payoffs where date(expect_date)< date(now()) and state = 0 "
        new_cursor.execute(sql)
        payoffs = new_cursor.fetchall()
        for payoff in payoffs:
            assetId=payoff["asset_id"]
            investId=payoff["investment_id"]
            payoffId=payoff["payoff_id"]
            payoffIdSuffix=int(str(payoffId)[-2:])

            state=payoff["state"]
            repayId=payoff["repayment_id"]
            #如果repayId已经回款，那么就设置payoff为回款的。
            sql="select state from product.t_repayments where repayment_id=%d " % (repayId)
            new_cursor.execute(sql)
            repayRows = new_cursor.fetchall()
            for repayRow in repayRows:
                state=repayRow["state"]
                if state == 2 or state == 3 :
                    updateSql="update inves.t_investment_payoff_%02d set state = 3,update_time=now() where payoff_id=%d and repayment_id=%d and state =0 ;\n" % (payoffIdSuffix,payoffId,repayId)
                    updateSqls="update inves.t_investment_payoffs set state = 3,update_time=now()  where payoff_id=%d and repayment_id=%d and state = 0 ;\n" % (payoffId,repayId)
                    f.write(updateSql)
                    f.write(updateSqls)

genSql()