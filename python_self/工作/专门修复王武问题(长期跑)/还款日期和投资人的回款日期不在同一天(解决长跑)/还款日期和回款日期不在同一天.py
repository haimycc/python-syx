import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def setDate():
    with open("./updatesql.20170224","a+") as f:
        sql="select a.payoff_id as aPayoffId,a.asset_type,a.asset_pool,b.repayment_id as bRepayId,a.expect_date as aDate,b.expect_date as bDate  from invest.t_investment_payoffs a ,product.t_repayments b where a.repayment_id=b.repayment_id  and date(a.expect_date) != date(b.expect_date) "
        new_cursor.execute(sql)
        rows = new_cursor.fetchall()
        for row in rows:
            payoffId=row["aPayoffId"]
            payoffIdSuffix=int(str(payoffId)[-2:])
            repayId=row["bRepayId"]
            payoffDate=row["aDate"]
            repayDate=row["bDate"]
            updateSql="update invest.t_investment_payoff_%02s set expect_date = '%s'  where payoff_id=%d and expect_date = '%s' ;\n" % (payoffIdSuffix,repayDate,payoffId,payoffDate)
            updateSqls="update invest.t_investment_payoffs set expect_date = '%s'  where payoff_id=%d and expect_date = '%s' ;\n" % (repayDate,payoffId,payoffDate)
            f.write(updateSql)
            f.write(updateSqls)


setDate()