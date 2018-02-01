import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def gensql():
    with open("updatesql.20170222", "a+") as f:
        for idx in range(0,100):
            sql="select * from invest.t_investment_payoff_%02d  where state = 3 and expect_principal != actual_principal and actual_principal =0 " % (idx)
            new_cursor.execute(sql)
            payoffs = new_cursor.fetchall()
            for payoff in payoffs:
                payoffId=payoff["payoff_id"]
                actualPrincipal=payoff["actual_principal"]
                expectPrincipal=payoff["expect_principal"]
                payffIdSuffix=int(str(payoffId)[-2:])
                sql="update invest.t_investment_payoff_%02d set actual_principal = expect_principal " \
                    "where " \
                    "payoff_id= %d and state = 3 and actual_principal = %d and expect_principal = %d ;\n " % (payffIdSuffix,payoffId,actualPrincipal,expectPrincipal)
                f.write(sql)

            sql="select * from invest.t_investment_payoff_%02d  where state = 3 and expect_interest != actual_interest and actual_interest =0 " % (idx)
            new_cursor.execute(sql)
            payoffs = new_cursor.fetchall()
            for payoff in payoffs:
                payoffId=payoff["payoff_id"]
                actualInterest=payoff["actual_interest"]
                expectInterest=payoff["expect_interest"]
                payffIdSuffix=int(str(payoffId)[-2:])
                sql="update invest.t_investment_payoff_%02d set actual_interest = expect_interest " \
                    "where " \
                    "payoff_id= %d and state =3 and actual_interest = %d and expect_interest = %d ;\n " % (payffIdSuffix,payoffId,actualInterest,expectInterest)
                f.write(sql)

            sql = "select * from invest.t_investment_payoff_%02d  where state = 3 and expect_add_interest != actual_add_interest and actual_add_interest =0 " % (idx)
            new_cursor.execute(sql)
            payoffs = new_cursor.fetchall()
            for payoff in payoffs:
                payoffId = payoff["payoff_id"]
                actualAddInterest = payoff["actual_add_interest"]
                expectAddInterest = payoff["expect_add_interest"]
                payffIdSuffix = int(str(payoffId)[-2:])
                sql = "update invest.t_investment_payoff_%02d set actual_add_interest = expect_add_interest " \
                      "where " \
                      "payoff_id= %d and state = 3 and actual_add_interest = %d and expect_add_interest = %d ;\n " % (
                      payffIdSuffix, payoffId, actualAddInterest, expectAddInterest)
                f.write(sql)


gensql()