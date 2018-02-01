import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

#老平台
old_conn = mysql.connector.connect(host='192.168.0.220',user='root',password='123456', database='toulf')
old_cursor = old_conn.cursor(dictionary=True)
#新平台
new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def genSql():
    with open('./3updateInvestSums', 'a+') as f:
        for idx in range(0,100):
            sql="update invest.t_investment_sums a,invest.t_investment_sum_%02d b " \
                "set " \
                "a.old_loan_invest_sum=b.old_loan_invest_sum," \
                "a.old_loan_invest_payoff=b.old_loan_invest_payoff," \
                "a.old_loan_invests=b.old_loan_invests," \
                "a.old_plan_invest_sum=b.old_plan_invest_sum," \
                "a.old_plan_invest_payoff=b.old_plan_invest_payoff " \
                " where " \
                "a.investor_uid=b.investor_uid ;\n" % (idx)
            f.write(sql)


genSql()