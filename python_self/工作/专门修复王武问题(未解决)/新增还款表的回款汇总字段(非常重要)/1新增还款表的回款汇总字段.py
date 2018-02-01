import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("1新增还款汇总表","a+") as f:
        for idx in range(0,100):
            sql1="alter table product.t_repayment_%02d " \
                "add column expect_payoff_principal bigint(20) NOT NULL DEFAULT '0' COMMENT '本期预计归还给所有投资人的本金'," \
                "add column expect_payoff_interest bigint(20) NOT NULL DEFAULT '0' COMMENT '本期预计归还给所有投资人的利息' ;\n" % (idx)
            sqls="alter table product.t_repayments " \
                 "add column expect_payoff_principal bigint(20) NOT NULL DEFAULT '0' COMMENT '本期预计归还给所有投资人的本金'," \
                 "add column expect_payoff_interest bigint(20) NOT NULL DEFAULT '0' COMMENT '本期预计归还给所有投资人的利息' ;\n"
            f.write(sql1)
            f.write(sqls)


handler()


