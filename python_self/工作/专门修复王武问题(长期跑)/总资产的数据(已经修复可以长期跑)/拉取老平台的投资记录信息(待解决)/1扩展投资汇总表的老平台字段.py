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
    with open('./1updateInvestSums', 'a+') as f:
        for idx in range(0,100):
            sql="alter table invest.t_investment_sum_%02d " \
                "add old_loan_invest_sum bigint(20) NOT NULL default 0 COMMENT '老平台定期理财累计投资金额'," \
                "add old_loan_invest_payoff bigint(20) NOT NULL default 0 COMMENT '老平台定期理财已经赚取收益'," \
                "add old_loan_invests bigint(20) NOT NULL default 0 COMMENT '老平台定期理财投资次数'," \
                "add old_plan_invest_sum bigint(20) NOT NULL default 0 COMMENT '老平台理财计划投资金额'," \
                "add old_plan_invest_payoff bigint(20) NOT NULL default 0 COMMENT '老平台理财计划已经赚取收益'; \n" % (idx)
            f.write(sql)
        sql = "alter table invest.t_investment_sums " \
              "add old_loan_invest_sum bigint(20) NOT NULL default 0 COMMENT '老平台定期理财累计投资金额'," \
              "add old_loan_invest_payoff bigint(20) NOT NULL default 0 COMMENT '老平台定期理财已经赚取收益'," \
              "add old_loan_invests bigint(20) NOT NULL default 0 COMMENT '老平台定期理财投资次数'," \
              "add old_plan_invest_sum bigint(20) NOT NULL default 0 COMMENT '老平台理财计划投资金额'," \
              "add old_plan_invest_payoff bigint(20) NOT NULL default 0 COMMENT '老平台理财计划已经赚取收益'; \n"
        f.write(sql)

genSql()