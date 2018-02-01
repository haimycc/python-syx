import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    allNum=0
    with open("2根据投资回款表更新还款表","a+") as f:
        #检查回款表分表和总表是否有差异
        for idx in range(0,100):
            sql="select count(1) as num from product.t_repayment_%02d " % (idx)
            new_cursor.execute(sql)
            rows = new_cursor.fetchall()
            for row in rows:
                num=row["num"]
                allNum=allNum+num
        print(allNum)
        sql="select count(1) as num from product.t_repayments "
        new_cursor.execute(sql)
        rows = new_cursor.fetchall()
        for row in rows:
            num = row["num"]
            print(num)

        #检查回款表和还款表是否有差异
        for idx in range(0,100):
            sql="select count(1) as num from invest.t_investment_payoff_%02d a,invest.t_investment_payoffs b " \
                "where " \
                "a.payoff_id=b.payoff_id and " \
                "a.expect_principal!=b.expect_principal and " \
                "a.expect_interest!=b.expect_interest and " \
                "a.actual_principal!=b.actual_principal and " \
                "a.actual_interest!=b.actual_interest " % (idx)
            new_cursor.execute(sql)
            rows = new_cursor.fetchall()
            for row in rows:
                num=row["num"]
                if num > 0 :
                    print("error")

        #根据回款总表去更新还款总表
        sql="select repayment_id,ifnull(sum(expect_principal),0) as principal,ifnull(sum(expect_interest),0) as interest from invest.t_investment_payoffs group by repayment_id "
        new_cursor.execute(sql)
        rows = new_cursor.fetchall()
        for row in rows:
            repayId = row["repayment_id"]
            repayIdSuffix= int(str(repayId)[-2:])
            principal=row["principal"]
            interest=row["interest"]
            sql="update product.t_repayment_%02d set expect_payoff_principal=%d,expect_payoff_interest=%d  where repayment_id=%d ;\n" % (repayIdSuffix,principal,interest,repayId)
            sqls="update product.t_repayments set expect_payoff_principal=%d,expect_payoff_interest=%d  where repayment_id=%d ;\n" % (principal,interest,repayId)
            f.write(sql)
            f.write(sqls)







handler()
